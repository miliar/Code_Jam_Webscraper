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

    int n,m,k;
    cin>>n>>m>>k;
    int h; bool sets[n+1];
    memset(sets,false,sizeof(sets));
    for(int i=1;i<=m;i++)
       {
          scanf("%d",&h);sets[h]=true;
       }
    int bn=1;bool flg=false;
    int u,v;int i;
    if(sets[1]) flg=true;
    if(flg)
    {for(int l=1;l<=k;l++)
    {
        scanf("%d %d",&u,&v);}}
    else  {
    for( i=1;i<=k;i++)
    {
        scanf("%d %d",&u,&v);
        if(!flg)
        {
        if(u==bn)
        {
            bn=v;
            if(sets[v])
            {
                flg=true;   break;
            }
        }
        else if(v==bn)
        {
            bn=u;
            if(sets[u])
            {
                flg=true;break;}
        }  }
     /*
     	int i;
        for(i=0;i<n;i++)
        	  printf("%d ",sets[i]);
        printf("\n");
  */
    }
    for(int j=i+1;j<=k;j++)
        {
            scanf("%d %d",&u,&v);
        } }
    printf("%d",bn);
    return 0;
}
