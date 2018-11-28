#include <iostream>
using namespace std;

int main(void) {
    int t,a,b,flag=0,i;
    cin>>t;
    int N[t];
    for(i=0;i<t;i++){
        cin>>N[i];
    }
    for(i=0;i<t;i++){   
        while(N[i]>0){
            flag=0;
            a=N[i]%10;
            b=N[i]/10;
            while(a>=b%10){
                a=b%10;
                b=b/10;
                if(b==0){
                    if(a>=b){
                        flag=1;
                         break;
                    }
                    else{
                    break;
                    }
                }
            }
            if(flag==1){
            cout<<"Case #"<<i+1<<": "<<N[i]<<endl;
            break;
            }
            N[i]--;
        }
    }
	return 0;
}
