#include<iostream>
#include<cmath>

using namespace std;

int main(){
    int cases;
    cin>>cases;
    
    int R=0;
    int C=0;
    char letra;
    char car;
    int cuenta=0;
    int interche=0;
    bool flag=false;
    int falto=-1;
    for(int i=0;i<cases;i++){
        falto=-1;
        cin>>R>>C;

        char ar[R][C];

        for(int row=0;row<R;row++){
            flag=false;
            interche=0;
            for(int col=0;col<C;col++){
                cin>>car;
                if(car=='?'){
                    interche+=1;
                    cuenta+=1;
                    if(flag){
                        ar[row][col]=letra;
                    }
                }
                else{
                    letra=car;
                    if(flag==false){

                    cuenta+=1;
                    flag=true;
                    for(int cun=0;cun<cuenta;cun++){
                        ar[row][cun]=letra;
                        //cout<<letra;
                    }
                    cuenta=0;
                    }
                    else{
                        ar[row][col]=letra;
                        //cout<<letra;
                    }

                }

                if(interche==C){
                    if(row==(falto+1)){
                        falto=row;
                        //cout<<falto;
                   
                    } 
                    else{
                        for(int col2=0; col2<C;col2++ ){
                        ar[row][col2]=ar[row-1][col2];
                    }
                        

                    }
                

                }
            }
        }

        cout<<"Case #"<<i+1<<":"<<endl;
        if(falto>=0){
            //cout<<falto<<endl;
            for(int row=0;row<falto+1;row++){
            for(int col3=0; col3<C;col3++ ){
                        ar[row][col3]=ar[falto+1][col3];
            }
            }
        }

        
        for(int row=0;row<R;row++){
            for(int col=0;col<C;col++){
                cout<<ar[row][col];
            }
            cout<<endl;
        }
        

    }
}