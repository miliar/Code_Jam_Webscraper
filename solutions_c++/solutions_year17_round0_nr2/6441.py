#include <iostream>
#include <string>

using namespace std;

int main()
{
   int t;
   cin>>t;
   for(int i=0;i<t;i++){
      string N;
      cin>>N;
      int len = N.length();
      for(int j=1;j<len;){
         if(N[j] < N[j-1]){
            int pivot = -1;
            if(j==1){
               if(N[j-1] == '1')N[j-1] = 0;
               else N[j-1] = ((N[j-1] - '0') - 1)  + '0';
            }
            else{
               pivot = j;
               j--;
               while(j && ((N[j-1] -'0') > ((N[j] - '0') - 1))){
                  N[j] = '9';
                  j--;
               }
               if(N[j] == '1')N[j] = 0;
               else{
                  N[j] = ((N[j] - '0') - 1)  + '0';
               }
               j=pivot;
            }

            while(j<len){
               N[j] = '9';
               j++;
            }
         }
         else j++;
      }
      if(N[0] == 0)N = N.substr(1);
      cout<<"Case #"<<i+1<<": "<<N<<endl;
   }
   return 0;
}
