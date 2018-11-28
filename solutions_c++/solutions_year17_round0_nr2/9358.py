#include <bits/stdc++.h>
using namespace std;

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
  set<int> vtr;
  int tests;
  cin>>tests;
  for(int i=1;i<=tests;i++)
  {
        int n,k,j;
        cin>>n;
        //cout<<n<<" ";

        if(n<19)
		{
         cout<<"Case #"<<i<<": "<<n<<endl;
         continue;
        }

        int x;
        for(k=n;k>0;k--)
		{
            //cout<<k<<endl;
            vector<int> vtr1;
            vector<int> vtr;
        	for(j=k;j>0;j=j/10)
			{
            x=j%10;
            vtr.push_back(x);
            }
        
       reverse(vtr.begin(),vtr.end());
       vtr1=vtr;
       sort(vtr1.begin(),vtr1.end());
       
       if(vtr==vtr1)
         {
		 	cout<<"Case #"<<i<<": "<<k<<endl;
		 	break;
		 }
		 
     	}
    }

   return 0;
}
