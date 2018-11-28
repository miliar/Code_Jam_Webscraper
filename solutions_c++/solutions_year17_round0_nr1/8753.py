/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: invitado
 *
 * Created on 8 de abril de 2017, 02:53 PM
 */

#include <cstdio>
#include <string>
#include <unordered_map>
#include <utility>

using namespace std;

typedef pair<int,int> ii;

int t, k, p, m, f, mm, c = 1;
char x[15];
unordered_map <string,int> a;
ii in;

int main(int argc, char** argv) {
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.out","w",stdout);
    scanf("%d", &t);
    while(t--){
        a.clear(); f = 0;
        scanf("%s %d", x , &k);
        string aux(x);
        do{
            mm = 0;
            for (int i = 0; i < k; i++)
                if (aux[i] == '-') mm++;
            
            int actualMinus = mm;
            in = ii(0,k-1);
            for (int i = 1; i < aux.size()-k+2; i++){
                if (aux[i-1] == '-') actualMinus--;
                if (aux[i+k-1] == '-') actualMinus++;
                else if (i+1 >= aux.size()-k+1 || actualMinus <= mm) continue;
                if (actualMinus >= mm){
                    mm = actualMinus;
                    in = ii(i,i+k-1);
                }
            }
            
            if (mm == 0) break;
            
            for (int i = in.first; i <= in.second; i++){
                aux[i] == '+' ? aux[i] = '-' : aux[i] = '+';
            }
            //printf("ACTUAL %s FLIPS %d\n", aux.c_str(), f);
            f++;
            if (!a[aux]) a[aux] = true;
            else break;
        }while(mm != 0);
        
        if (mm == 0){
            printf("Case #%d: %d\n", c++, f);
        }else{
            printf("Case #%d: IMPOSSIBLE\n", c++);
        }
    }
    return 0;
}

