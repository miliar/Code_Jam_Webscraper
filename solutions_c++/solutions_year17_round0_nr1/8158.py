#include<bits/stdc++.h>
using namespace std;
int mypowerfun(int arr,int b)
{
	if(b==0)
	return 1;
	if(b==1)
	return arr;
	int x=mypowerfun( arr,b/2);
	if(b%2==0)
	return x*x;
	else
	return x*x*arr;
}
void pri_arr(int arr[],int n )
{
   int i;
   for(i=0;i<n;i++)
	  printf("%d ",arr[i]);
   printf("\n");
}
void pri_vec(vector<int> a,int n)
{
for (std::vector<int>::iterator it = a.begin() ; it != a.end(); ++it)
    std::cout  << *it;
  std::cout << '\n';
}
int mygcd(int arr,int b)
{
	if (b != 0)
       return mygcd(b, arr%b);
    else
       return arr;
}
stack<char> s1;
int finding(string s,int n,int l,int j1);
int main()
{
    freopen("input.in","r",stdin);
freopen("output_file_name.out","w",stdout);
    string s;
    int t;cin>>t;
    int j=1;
    while(j<=t)
    {
    int l;cin>>s;cin>>l;
    int n=s.length();
    int temp=finding(s,n,l,j);j++;
    }
    return 0;
}
int finding(string s,int n,int l,int j1)
{
    int i=0,j,k,temp,ind=0;
    int cnt=0;
    while(i<n)
    {
    for(i=0;i<n;i++)
    {  if(s[i]=='-')
        {
                if(i>=(n-l+1))
                {
                    cout<<"Case #"<<j1<<":"<<" "<<"IMPOSSIBLE"<<endl;
                    ind=1; break;
                }
            j=i;
            while(j<i+l)
            {
                if(s[j]=='+') s[j]='-';
                else s[j]='+';
                j++;
            } cnt++;
        }
    }
    if(ind==1){
        break;
    }
    }
    if(ind!=1){
    cout<<"Case #"<<j1<<":"<<" "<<cnt<<endl;
    }
    return 0;
}
