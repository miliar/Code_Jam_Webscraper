#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <cassert>
using namespace std;
#define rep(i,n) for(int i=1;i<=(n);++i)
#define rep2(i,a,b) for(int i=(a);i<=(b);++i)
int n,nk;
int ind[102];
int tdp[4][102][102][102][102];
int inc[5];
void task()
{
	scanf("%d%d",&n,&nk);
	memset(inc,0,sizeof inc);
	rep(i,n)
	{
		scanf("%d",&ind[i]);
		inc[ind[i]%nk]++;
	}
	//cout<<inc[0]<<","<<inc[1]<<","<<inc[2]<<","<<inc[3]<<endl;
	printf("%d\n",tdp[nk-1][inc[0]][inc[1]][inc[2]][inc[3]]);		
}
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int nt;scanf("%d",&nt);
	memset(tdp,-37,sizeof tdp);
	n=100;
						#define tdp tdp[nk-1]
	rep2(nk,2,4)
	{
		tdp[0][0][0][0]=0;
		rep2(i,0,n)
		{
			rep2(j,0,n)
			{
				rep2(k,0,n)
				{
					rep2(l,0,n)
					{
						if(tdp[i][j][k][l]>=0)
						{
							#define UPD(i,j,k,l) ((((i)*0+(j)*1+(k)*2+(l)*3)%nk==0)?1:0)
							tdp[i+1][j][k][l]=max(UPD(i,j,k,l)+tdp[i][j][k][l],tdp[i+1][j][k][l]);
							tdp[i][j+1][k][l]=max(UPD(i,j,k,l)+tdp[i][j][k][l],tdp[i][j+1][k][l]);
							tdp[i][j][k+1][l]=max(UPD(i,j,k,l)+tdp[i][j][k][l],tdp[i][j][k+1][l]);
							tdp[i][j][k][l+1]=max(UPD(i,j,k,l)+tdp[i][j][k][l],tdp[i][j][k][l+1]);
						}
					}
				}
			}
		}
	}
	rep(i,nt){printf("Case #%d: ",i);task();fflush(stdout);}
}

