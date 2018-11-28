//zadanie: Problem A. Alphabet Cake - Google Code Jam 201//login: magda332241#include<iostream>#include<cmath>#include<stdint.h>#include <vector>using namespace std;int main(){   ios::sync_with_stdio(false);   cin.tie(NULL);   int T, R,C, f=0, g=0;//f - cos sie pojawilo w linii, g - coss sie pojawilo wgl
   int licznik, licz_k, l;//licznik - ile znakow zapytania od poczatku w rzedzie, licz_k - ile kolumn tylko ze znakami zapytania;
   char a, ap;//a - wczytany znak, ap - poprzedni znak nie bedacy '?'
      cin >> T;      for (int o=0; o<T; o++){
   cout << "Case #" << o+1<<": "<<'\n';
   vector<char> v;   licznik=0; f=0; g=0;licz_k=-1;      cin >> R >> C;      for (int i=0; i<R; i++){
      licznik = 0;        for(int p=0; p<C; p++){
                        cin >> a;
            //v.push_back(a);
            if(a!='?'){
              for(int q=0; q<=licznik; q++){
              cout << a; 
              v.push_back(a);}
              f=1;ap=a;g=1;licznik=0;
            }
            else{
              if(f==1){cout << ap; v.push_back(ap);}
              else {licznik ++;}
              }
            if(licznik==C){
              if(g!=0){//jesli cos sie pojawilo to przepisujemy poprzednia linijke
                for(int q=0; q<C; q++){
                  l=v.size();
                  cout << v[l-C+q];
                  //v.push_back(v[l-C+q-1]);
                }
              }
              else licz_k++;
            }
           }
           if(g!=0){cout << '\n';}
            if(f!=0){
              for(int q=0; q<=licz_k; q++){
                for(int w=0; w<C; w++){
                  l=v.size();
                  cout << v[l-C+w];
                }
                cout << '\n';
              }
              licz_k=-1;
              f=0;
            }
                    }
        licz_k=0;      }       return 0;}