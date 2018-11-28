#include <bits/stdc++.h>
using namespace std;

int main() {
	int t = 0;
	scanf("%d", &t);
	
	for(int i = 1; i <= t; i++){
	    int r = 0;
	    int c = 0;
	    scanf("%d %d", &r, &c);
	    
	    char cake[r][c];
	    
	    for(int j = 0; j < r; j++){
	        char s[30];
	        scanf("%s", s);
	        
	        for(int k = 0; k < c; k++){
	            cake[j][k] = s[k];
	        }
	    }
	    
	    vector<char> letter (c,'?');
	    for(int j = 0; j < r; j++){
	        for(int k = 0; k < c; k++){
	            if(cake[j][k] != '?'){
	                
	                if(letter[k] == '?'){
	                    for(int q = 0; q < j; q++){
	                        cake[q][k] = cake[j][k];
	                    }
	                }
	                
	                letter[k] = cake[j][k];
	                
	                continue;
	            }
	            cake[j][k] = letter[k];
	        }
	    }
	    
	    int first = 0;
	    for(int k = 0; k < c; k++){
	        if(letter[k] != '?'){
	            first = k;
	            break;
	        }
	    }
	    
	    int last = 0;
	    for(int k = c-1; k >= 0; k--){
	        if(letter[k] != '?'){
	            last = k;
	            break;
	        }
	    }
	    
	    for(int k = 0; k < first; k++){
	        letter[k] = letter[first];
	        for(int j = 0; j < r; j++){
	            cake[j][k] = cake[j][first];
	        }
	    }
	    
	    for(int k = last+1; k < c; k++){
	        letter[k] = letter[last];
	        for(int j = 0; j < r; j++){
	            cake[j][k] = cake[j][last];
	        }
	    }
	    
	    for(int k = 0; k < c; k++){
	        if(letter[k] != '?') continue;
	        for(int j = 0; j < r; j++){
	            cake[j][k] = cake[j][k-1];
	        }
	    }
	    
	    printf("Case #%d:\n", i);
	    for(int j = 0; j < r; j++){
	        for(int k = 0; k < c; k++){
	            printf("%c",cake[j][k]);
	        }
	        puts("");
	    }
	    
	}
	return 0;
}
