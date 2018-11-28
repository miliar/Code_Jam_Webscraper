#include <iostream>
#define MAXRC 30
using namespace std;

char cake[MAXRC][MAXRC];
bool letra[MAXRC];

int main (){
    int teste;
    cin >> teste;


    for(int t=1;t<=teste;t++){
        int r,c;
        cin >> r >> c;

        for(int i=0;i<MAXRC;i++)
            letra[i] = false;

        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                cin >> cake[i][j];
            }
        }

        char car;
        bool flag;
        int minC,maxC,cAtual,linha;
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                car = cake[i][j];

                if(!letra[car-'A']){
                    letra[car-'A'] = true;

                    minC = maxC = j;

                    for(int k=0;k<c;k++){
                        if(cake[i][k] == '?' || cake[i][k]==car){
                            cake[i][k] = car;
                            if(k>maxC)maxC = k;
                            if(k<minC)minC = k;
                        }else{
                            if(k>=j)break;
                        }
                    }

                    flag = true;

                    for(int l=i+1;l<r && flag;l++){
                        for(int k=minC;k<=maxC && flag;k++){
                            if(cake[l][k] != '?' && cake[l][k] != car)
                                flag = false;
                        }

                        if(flag){
                            for(int k=minC;k<=maxC;k++){
                                cake[l][k] = car;
                            }
                        }
                    }

                    flag = true;

                    for(int l=i-1;l>=0 && flag;l--){
                        for(int k=minC;k<=maxC && flag;k++){
                            if(cake[l][k] != '?' && cake[l][k] != car)
                                flag = false;
                        }

                        if(flag){
                            for(int k=minC;k<=maxC;k++){
                                cake[l][k] = car;
                            }
                        }
                    }
                }


            }

        }



        cout << "Case #" << t << ":" << "\n";
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                cout << cake[i][j];

            }
            cout << "\n";
        }
    }

    return 0;
}
