# AlertaAqui — Entrega RPA (UiPath) · FIAP

Robô UiPath que lê os boletins da Defesa Civil (sistema legado **sem API**, simulado pela planilha `alertas_defesa_civil.xlsx`) e cadastra cada alerta no formulário web do painel admin do AlertaAqui (`form.html`).

## Conteúdo

| Arquivo | O que é |
|---|---|
| `docs/rpa.md` / `docs/rpa.pdf` | Documentação: processo, assessment (27/30 → apto para RPA), diagnóstico RPA vs API + roadmap, BPM As-Is/To-Be (mermaid), business case (premissas marcadas), roteiro do vídeo de 3 min, passo a passo no Studio (5 min) |
| `alertas_defesa_civil.xlsx` / `.csv` | 10 boletins de exemplo (aba `Alertas`; colunas Regiao, NivelRisco, Mensagem, Data). CSV com `;` e UTF-8 |
| `form.html` | Painel admin simulado (IDs `regiao`, `nivel`, `mensagem`, `data`, `btnEnviar`), validação e lista persistida em localStorage com botão limpar |
| `UiPath/AlertaAquiRPA/` | `project.json` + `Main.xaml` (Windows-Legacy, VB) e cópias da planilha e do form (caminhos relativos) |
| `_build/` | Scripts Python usados para gerar o xlsx e o HTML/PDF |

## Fluxo do robô

Assign urlForm → Read Range (workbook) → Open Browser (Chrome, `file:///.../form.html`) → For Each Row → Try Catch { Type Into regiao · Select Item nivel · Type Into mensagem · Type Into data · Click btnEnviar · Log Message } Catch System.Exception → Log Message (Error) → Log final com totais.

## Como rodar

1. Abrir `UiPath/AlertaAquiRPA/project.json` no UiPath Studio (Community é grátis), com a extensão Chrome do UiPath instalada.
2. Run. Resultado esperado: 10 alertas na lista do form e `Sucesso: 10 | Erros: 0` no Output.

> **Aviso:** o `Main.xaml` foi escrito à mão e **não foi aberto/testado no UiPath Studio**. Se o Studio reclamar, monte em ~5 min seguindo a seção 8 de `docs/rpa.md` (cada atividade, propriedade e seletor está lá).

## Business case (resumo — premissas/estimativas)

600 boletins/mês × 8 min + retrabalho = 84,5 h/mês × R$ 60/h ≈ **R$ 60.840/ano** manual; custo estimado UiPath produção ≈ R$ 28.600/ano → **economia líquida ≈ R$ 32.240/ano**, payback ≈ 5,6 meses.
