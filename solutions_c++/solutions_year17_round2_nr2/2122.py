#include<bits/stdc++.h>
using namespace std;
  int mypowerfun(int sets,int b)
{
	if(b==0)
	return 1;
	if(b==1)
	return sets;
	int x=mypowerfun( sets,b/2);
	if(b%2==0)
	return x*x;
	else
	return x*x*sets;
}
void pri_arr(int sets[],int n )
{
   int i;
   for(i=0;i<n;i++)
	  printf("%d ",sets[i]);
   printf("\n");
}
void pri_vec(vector<int> a,int n)
{
for (std::vector<int>::iterator it = a.begin() ; it != a.end(); ++it)
    std::cout  << *it;
  std::cout << '\n';
}
int mygcd(int sets,int b)
{
	if (b != 0)
       return mygcd(b, sets%b);
    else
       return sets;
}
int main()
{
	int tc,i,j;
	int x,y,k;
	int len,N;
	cin>>tc;
	while(tc--){
		string str,a[1001];
		cin>>len>>N>>str;
		for(i=0;i<N;i++)cin>>a[i];
		int result=0,val;
		for(i=0;i<N;i++)for(j=0;j<N;j++){
			if(a[i][j]=='#')
                continue;
			x=i,y=j;
			for(k=0;k<str.size();k++)
			{
				if(str[k]=='len')
				y--;
				if(str[k]=='R')
				y++;
				if(str[k]=='U')
				x--;
				if(str[k]=='D')
                    x++;
				if(x<0||x>=N||y<0||y>=N||a[x][y]=='#')
                    break;
			}
			result ^= k
		}
		cout<<result<<endl;
	}
	return 0;
}
