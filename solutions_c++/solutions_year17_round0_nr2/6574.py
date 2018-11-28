#include<bits/stdc++.h>

using namespace std;

int main()
{
  int t;
  cin>>t;
  for(int q=1;q<=t;q++)
  {
    int i=0,j;
    char n[20]={0};
    cin>>n;
    if(int(n[0])<58 && strlen(n)==1)
      cout<<"Case #"<<q<<": "<<n<<endl;
    else
    {
      for(i=strlen(n)-1;i>=0;i--)
      {
        if(n[i]<n[i-1])
        {
        	if(n[i-1]=='0')
        		n[i-1]='9';
        	else
        		n[i-1]=char(int(n[i-1])-1);
        	j=i;
        	for(;i<strlen(n);i++)
        		n[i]='9';
        	i=j;
        }
      }
      cout<<"Case #"<<q<<": ";
      for(i=0;i<strlen(n);)
      {
      	if(n[i]==48)
      		i++;
      	else
      		break;
      }
      for(;i<strlen(n);i++)
      	cout<<n[i];
      cout<<endl;
    }
  }
  return 0;
}
