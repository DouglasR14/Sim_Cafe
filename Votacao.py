import streamlit as st
from PIL import Image

# Configurar o layout e o tema da página
st.set_page_config(page_title="Sim/Café", page_icon="💀")

# Função para exibir a página da enquete
def pagina_votacao():
    # Título e subtítulo
    st.markdown("<h1 style='text-align: center; color: red;'>💀💀💀Sim/Café💀💀💀</h1>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center; font-size: 12px; color: white;'>Mais uma das promessas vazias do Dener que não foram concretizadas</h6>", unsafe_allow_html=True)

    # Inicializar contagem de votos
    if "votos" not in st.session_state:
        st.session_state.votos = {"A": 0, "B": 0, "C": 0}

    # Opções de voto
    opcoes = [
        "Alemão", 
        "***Dener***", 
        "Denise", 
        "Douglas", 
        "João Marcos", 
        "Igor", 
        "Lucas Chaves", 
        "Lucas Valentim", 
        "Luiz", 
        "Márcio", 
        "Régis", 
        "Sttanley", 
        "Vivi"
    ]

    # Votação com HTML para estilização
    voto = st.radio("Quem você deseja que seja agraciado com a oportunidade de fornecer o próximo café da área?:", options=opcoes)

    # Remover a formatação HTML para guardar o voto corretamente
    voto_limpo = voto.split(">")[-1].split("<")[0]

    # Botão para enviar o voto
    if st.button("Votar"):
        if voto_limpo == "Douglas":  # Condição para erro
            st.error("Erro: Opção Inválida, canalha! Tente novamente.")
        else:
            st.success(f"Você votou na opção: {voto_limpo}")

    # Verificar resultados com Dener sempre 100%
    if st.button("Ver resultados"):
        # Manipular os resultados para Dener ser sempre 100%
        resultado_manipulado = {op: (100 if op == "Dener" else 0) for op in ["Alemão", "Dener", "Denise", "Douglas", "João Marcos", "Igor", "Lucas Chaves", "Lucas Valentim", "Luiz", "Márcio", "Régis", "Sttanley", "Vivi"]}
        
        st.write("Contagem de votos atual:")
        for opcao in resultado_manipulado.keys():
            st.write(f"{opcao}: {resultado_manipulado[opcao]}% votos")
        
        # Exibir frase abaixo dos resultados
        st.write("O escolhido para pagar o próximo café é: Dener 💀")

    # Frase no final da página
    st.markdown("<h5 style='text-align: center; font-size: 12px; color: white;'>'Acredite na justiça, mas não a que emana dos demais e sim na tua própria'</h5>", unsafe_allow_html=True)

# Executar a função de votação
if __name__ == "__main__":
    pagina_votacao()
