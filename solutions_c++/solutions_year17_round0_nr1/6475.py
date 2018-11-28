#include <iostream>
#include <string>

using namespace std;

int main()
{
   int t;
   cin>>t;
   string pancakes[1000];
   int flipper[1000];
   for(int i=0;i<t;i++){
      cin>>pancakes[i];
      cin>>flipper[i];
   }
   for(int i=0;i<t;i++){
      string panck = pancakes[i];
      int flipr = flipper[i];

      int len = panck.length();
      int cnt =0;
      bool possible = true;
      for(int j=0;j<len;){
        if(panck[j] == '+'){
           j++;
        }
        else {
          int mini = 2000;
          while(panck[j] == '+')j++;
          
          if(j > len -1)break;
          else{ 
             if(len-j < flipr){
                possible = false;
                break;
             }
             else cnt++;
          }

          for(int k=0;k<flipr;k++){
             if(panck[j] == '+'){
                if(mini > j)mini = j;
                panck[j] = '-';
                j++;
             }
             else
             {
                panck[j] = '+';
                j++;
             }
          }
          if(mini != 2000)j = mini;
        }
      }
      if(possible){
         cout<<"Case #"<<i+1<<": "<<cnt<<endl;
      }
      else{
        cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
      }
   }
   return 0;
}
