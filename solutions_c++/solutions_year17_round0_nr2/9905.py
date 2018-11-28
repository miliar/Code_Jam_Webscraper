#include <iostream>
using namespace std;
bool is_sort(string n)
{
    for(int i=1; i<n.length(); i++)
        if(n[i-1] > n[i]) return false;
    return true;
}

long long int areSorted(long long int n)
{
   string ans = to_string(n);
   loo:
   int flag=0;
   for(int i=1; i<ans.length(); i++)
   {
       if(!flag)
       {
       if(ans[i-1]>ans[i])
       {
           ans[i-1]=ans[i-1]-1;
           ans[i] = '9';
           flag=1;
       }
       }
       else
       ans[i] = '9';
   }
   if(!is_sort(ans)) goto loo;
   
   long long int a=0;
   int l=ans.length();
    int j=0;
    while(j<l)
    {
        a=a*10+(ans[j]-48);
        j++;
    }
    
    return a;
}
 

int main() {
	// your code goes here
	int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        long long int n;
        cin>>n;
        cout<<"Case #"<<i<<": "<<areSorted(n)<<endl;
    }
	return 0;
}