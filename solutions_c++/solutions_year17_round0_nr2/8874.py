
#include <cstdio>
#include <string>
#include <vector>

using namespace std;


int t, c= 1;
char x[40];

bool ordenado(string &aux){
    if (aux.size()==1) return true;
    for (int i = 0; i < aux.size()-1; i++){
        if (aux[i] > aux[i+1]){
            return false;
        }
    }
    return true;
}

char decrementar(char &A){
    switch(A){
        case '9':
            return '8';
        case '8':
            return '7';
        case '7':
            return '6';
        case '6':
            return '5';
        case '5':
            return '4';
        case '4':
        	return '3';
        case '3':
            return '2';
        case '2':
            return '1';
        case '1':
            return '0';
    }
}

void print(string &aux){
    int i = 0;
    while (aux[i] == '0') i++;
    printf("Case #%d: %s\n", c++, aux.c_str() + i);
}

int main(int argc, char** argv) {
    freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
    
    scanf("%d", &t);
    while (t--){
        scanf("%s", x);
        //printf("CADENA: %s\n", x);
        string aux(x);
        while (!ordenado(aux)){
            for (int i = aux.size()-1; i >= 0; i--){
            	//printf("A COMPARAR %c - %c\n", aux[i], aux[i-1]);
                if (aux[i] < aux[i-1]){
                	//printf("%c ES MENOR\n", aux[i]);
                    for (int j = i; j < aux.size(); j++){
                        aux[j] = '9';
                    }
                    aux[i-1] = decrementar(aux[i-1]);
                    break;
                }
            }
        }
        print(aux);
    }
    return 0;
}
