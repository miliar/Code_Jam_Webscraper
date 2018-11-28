#include<iostream>
#include<fstream>
using namespace std;
int main(){
long int i=0,j=0,k=0,input=0,largest=0,large=0,n=0,semi=0;
//cin>>n;
ifstream in;
in.open("B-small-attempt0.in");
in>>n;
 ofstream out;
 out.open("gg.txt");
for(i=1;i<=n;i++){
    in>>input;
    //cin>>input;
    while(input>0){
        largest=input;
        large=largest%10;
        while(largest>=1){
            largest=largest/10;
                if(largest!=0){
                   semi=largest%10;
                 if(semi<=large){
                    large=semi;
                 }
                 else{
                        break;
                 }
                 }
                 else{
                      //cout<<input<<endl;


                      out<<"case #"<<i<<": "<<input<<endl;
                        break;

               }

      }
      if(largest==0){
                   break;
              }
 input--;

}
}
in.close();
out.close();


return 0;}
