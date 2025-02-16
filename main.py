def find(pattern, text):

    # Função para extrair os subpadrões
    def extract_sub_patterns(pattern):
        sub_patterns = []
        current_pattern = ""
        i = 0
        while i < len(pattern):
            if (i + 2 < len(pattern)) and (pattern[i] == ' ') and (pattern[i+1] == 'U') and (pattern[i+2] == ' '):
                sub_patterns.append(current_pattern)
                current_pattern = ""
                i += 3
            else:
                current_pattern += pattern[i]
                i += 1
        sub_patterns.append(current_pattern)
        return sub_patterns

    # Extração dos subpadrões
    sub_patterns = extract_sub_patterns(pattern)

    # Busca no texto referente à cada subpadrão
    for sub_pattern in sub_patterns:
        pattern_length = len(sub_pattern)
        text_length = len(text)

        # Função de transição
        def transition(current_state, character):
            if current_state < pattern_length and sub_pattern[current_state] == character:
                return current_state + 1
            return 0

        # Processa o texto usando o autômato
        state = 0
        for i in range(text_length):
            state = transition(state, text[i])
            if state == pattern_length:
                print(f"subpadrão '{sub_pattern}' encontrado no index", i - pattern_length + 1)
                state = 0

# Exemplos de uso
#find("a", "umaa mangaa e duaas bbanaanaas")
#find("a U aa", "umaa mangaa e duaas bbanaanaas")
#find("aa U bb", "umaa mangaa e duaas bbanaanaas")
#find("/ U 1 U 2", "/123456789/")
