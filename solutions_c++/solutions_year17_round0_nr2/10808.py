#include<iostream>
#include<fstream>
using namespace std;
int nondecreasing(int n){
   int arr[10],num=n,t=0,result=9,len=0,flag=0,i;

   if(n/10==0){
    return n;
   }



   for(i=(3/4)*n;i<=n;i++){
     t=0;
     num=i;
     while(num>0){
        num=num/10;
        t++;
    }
     num=i;
     t=t-1;
     len=0;
     while(num>0){
        arr[t]=num%10;
        num=num/10;
        t--;
        len++;
     }

     for(t=0;t<=len-2;t++){
        if(arr[t+1]>=arr[t]){
            flag=1;

        }
        else{
            flag=0;
            break;
        }
     }
     if(flag==1){
        result=i;
     }
   }
    return result;

   }



int main(){
    int t;
    int n;
    int ans=0,num,i=0,j=1;

    ifstream in("input.txt");
    in>>t;

    ofstream out("output.txt");
   while(t--){
       in>>n;
       ans= nondecreasing(n);
       out<<"Case #"<<j<<": "<<ans<<"\n";
       j++;
       cout<<"Case #"<<j<<": "<<ans<<"\n";

    }

   out.close();
    in.close();
}


