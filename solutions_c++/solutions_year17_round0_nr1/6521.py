#include <bits/stdc++.h>
using namespace std;
int main()
{
     int test , cs = 1;
     scanf("%d",&test);
     while(test--){
         string s;
         int k;
         cin >> s >> k;
         int sz = s.size();
         int counter = 0;
         for(int i = 0 ; i<= sz-k ; i++){
             if(s[i] == '-'){
                 for(int j = 0 ; j< k ; j++){
                     if(s[i+j] == '-')
                     s[i+j] = '+';
                     else s[i+j] = '-';
                 }
                 counter++;
             }
             // cout << s << endl;
         }
         bool flag = 0;
         for(int i = 0 ; i< s.size() ; i++){
             if(s[i] == '-'){
                 printf("Case #%d: IMPOSSIBLE\n",cs++);
                 flag = 1;
                 break;
             }
         }
         if(flag == 0){
            printf("Case #%d: %d\n",cs++ , counter);
         }

     }
}