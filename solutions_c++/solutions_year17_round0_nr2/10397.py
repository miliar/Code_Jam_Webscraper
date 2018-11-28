#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

using namespace std;
bool acendente(unsigned long long num){

    unsigned long long numero=num;
    unsigned long long resto=num;
    bool acen=true;

        numero=numero/10;
        resto=resto%10;
        while(numero>0)
        {
          if((numero%10)<=resto){
                resto=numero%10;
                numero=numero/10;
            }else{
                acen=false;
                return acen;
            }
        }
    return acen;
}



int main()
{
    int t,i=0;
    unsigned long long num=0;
    scanf("%d",&t);

    for(i=1;i<=t;i++){
       cin>>num;
       for(;num>=1;num--){
            if(acendente(num)){
                break;
            }

       }
       cout<<"Case #"<<i<<": "<<num<<endl;
    }
    return 0;
}
