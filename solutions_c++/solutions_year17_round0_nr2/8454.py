#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

int main() 
{
	int t;
	cin>>t;
	
	vector<long long> v;
	v.push_back(10);
	for(int i=1;i<18;i++)
	{
	    v.push_back(v[i-1]*10);
	    //cout<<v[i]<<endl;
	}
	
	for(int i=1;i<=t;i++)
	{
	   long long num;
	   cin>>num;
	   string s,z,ans;
	   if(binary_search(v.begin(),v.end(),num))
	   {
	       ans = to_string(num-1);
	       
	   }
	   else
	   {
	   s= to_string(num);
	   z=s;
	   if(is_sorted(z.begin(),z.end()))
	   {
	       ans = z;
	   }
	   else
	   {
	       for(int i=z.size()-1;i>=1;i--)
	       {
	           char l = z[i];
	           char pl = z[i-1];
	           if(l=='0')
	           {l='9';pl--;}
	           else
	           {
	           if(l>=pl) continue;
	           int lv = l - '0',plv;
	           pl--;
	           lv = 9;
	           l = lv + '0';}
	           z[i] = l;
	           z[i-1] = pl;
	          ans=z;
	           if(is_sorted(z.begin(),z.end()))
        	   {
        	       ans = z;
        	       break;
        	   }
	       }
	   }
	   }
	   string ansf = "";
	   for(int j=0;j<ans.size();j++)
	   {
	       if(ans[j]!='0')
	       {
	           ansf+=ans[j];
	       }
	   }
	   //cout<<ans<<endl;
	   if(is_sorted(ansf.begin(),ansf.end()))
	   {
	      // cout<<"in if";
	       cout<<"Case #"<<i<<": ";
	        cout<<ansf<<endl;
	   }
	   else
	   {
	      // cout<<"in el";
	       for(int j=1;j<ansf.size();j++)
	       {
	           if(ansf[j]>=ansf[j-1])
	           continue;
	           ansf[j]=ansf[j-1];
	       }
	        cout<<"Case #"<<i<<": ";
	        cout<<ansf<<endl;
	   }
	   
	    
	}
	return 0;
}
