#include <iostream>

using namespace std;

int main()
{freopen("B-small-attempt1.in","r",stdin);
freopen("output_file_name.out","w",stdout);

int f;
cin>>f;
for(int j=0;j<f;j++){
   int N;
   cin>>N;
   for(int i=N;i>=1;i--){
       int x=i%10;
       int b=i;
       while(b!=0){
           if(b%10<=x){
               x=b%10;
               b=b/10;
               if(b==0)
               break;
           }
           else
               break;
        }
        if(b==0){
        cout<<"Case #"<<j+1<<": "<<i<<endl;
        break;
        }
   }
}
   return 0;
}
