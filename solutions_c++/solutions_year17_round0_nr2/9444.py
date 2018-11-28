#include <bits/stdc++.h>
using namespace std;

int main()
{
 ifstream myfile;
 ofstream outfile("output.txt");
  set<int> vtr;
  myfile.open ("input.txt");
  int tests;
  myfile>>tests;
  for(int i=1;i<=tests;i++){
        int n;
        myfile>>n;
        if(n<=19){
         outfile<<"Case #"<<i<<": "<<n<<endl;
         continue;
        }

        int x;
        for(int k=n;k>(n/2);k--){
        vector<int> vtr;
        vector<int> vtr1;
        for(int j=k;j>0;j=j/10){
            x=j%10;
            vtr.push_back(x);
            }

       reverse(vtr.begin(),vtr.end());
       vtr1=vtr;
       sort(vtr1.begin(),vtr1.end());

       if(vtr==vtr1){
                 outfile<<"Case #"<<i<<": "<<k<<endl;
                 break;
       }

    }
  }
   return 0;
}
