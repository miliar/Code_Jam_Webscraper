//Bismillahir Rahmanir Rahim
#include <bits/stdc++.h>
using namespace std;

#define MAX_V 5000
#define MAX_E 500000
#define INF 7777777

struct EDGE{
	long long v,c;
};
long long nV;
long long SRC,TNK;
long long eI;
EDGE Edge[MAX_E+7];	// edge list
long long Next[MAX_E+7]; // next pointer of vertex v
long long Last[MAX_V+7]; // last index of adj edge of vertex v
long long Dist[MAX_V+7];	// level from src
long long Start[MAX_V+7];// temporary used for last

inline void SetEdge( long long u,long long v,long long c )
{
    //cout<<u<<" edge "<<v<<endl;
	Edge[eI].v = v;
	Edge[eI].c = c;
	Next[eI] = Last[u];
	Last[u] = eI++;
	Edge[eI].v = u;
	Edge[eI].c = 0;
	Next[eI] = Last[v];
	Last[v] = eI++;
}

long long Q[MAX_V+7];
long long Frnt,End;

bool Bfs( void )
{
	Frnt = End = 0;
	Q[End++] = SRC;
	long long i;
	for( i=0;i<nV;i++){
		Dist[i] = INF;
	}
	Dist[SRC] = 0;
	long long u,v;
	while( Frnt<End ){
		u = Q[Frnt++];
		for( i=Last[u];i!=-1;i=Next[i]){
			v = Edge[i].v;
			if( !Edge[i].c || Dist[v]<INF ) continue;
			Dist[v] = Dist[u] + 1;
			Q[End++] = v;
		}
	}
	return Dist[TNK] < INF;;
}


long long AugmentPath( long long u,long long f )
{
	if( u==TNK ) return f;
	long long Tot = 0;
	for( long long &i = Start[u];i!=-1;i=Next[i] ){
		long long v = Edge[i].v;
		if( !Edge[i].c ) continue;
		if( Dist[v] != Dist[u]+1 ) continue;
		long long Tmp = AugmentPath( v,min( f,Edge[i].c ));
		Edge[i].c -= Tmp;
		Edge[i ^ 1].c += Tmp;
		Tot += Tmp;
		f -= Tmp;
		if( !f ) break;
	}
	return Tot;
}

long long MaxFlow( void )
{
	long long Flw = 0;
	while( Bfs()){
		memcpy( Start,Last,(nV)*sizeof(long long));
		Flw += AugmentPath( SRC,2*INF );
	}
	return Flw;
}

long long DD[100009];
long long U[109][109];

long long IN(long long x)
{
    return 2*x-1;
}

long long OUT(long long x)
{
    return 2*x;
}

int main()
{
    freopen("out.txt","rt",stdin);
    freopen("out1.txt","wt",stdout);
    long long i,j,k,l,n,m,cas,test,p,l1,l2,r1,r2,r,ans,now;

    cin>>test;
    for(cas=1;cas<=test;cas++)
    {
        cin>>n>>p;
        for(i=1;i<=n;i++)
        {
            cin>>DD[i];
        }

        eI = 0;
        memset( Last,-1,sizeof(Last));

        for(i=1;i<=n;i++)
        {
            for(j=1;j<=p;j++)
            {
                cin>>U[i][j];
            }
        }

        if(n==1)
        {
            ans=0;
            for(i=1;i<=p;i++)
            {
                now=U[1][i]/DD[1];
                for(j=max(1LL,now-1000);j<=now+1000;j++)
                {
                    if(U[1][i]*100>=90*j*DD[1] && U[1][i]*100<=110*j*DD[1]) { ans++; break; }
                }
            }

            printf("Case #%lld: %lld\n",cas,ans);
            continue;
        }

        for(i=1;i<=n;i++)
        {
            if(i==1)
            {
                for(j=1;j<=p;j++)
                {
                    SetEdge(0,IN((i-1)*p+j),1);
                }
            }
            else
            {
                for(j=1;j<=p;j++)
                {
                    for(k=1;k<=p;k++)
                    {
                        //cout<<"ll\n";
                        l1=U[i-1][j]*100;
                        l1/=90;
                        l1/=DD[i-1];
                        r1=U[i-1][j]*100;
                        r1/=110;
                        r1/=DD[i-1];
                        if(U[i-1][j]*100%(110*DD[i-1])) r1++;

                        l2=U[i][k]*100;
                        l2/=90;
                        l2/=DD[i];
                        r2=U[i][k]*100;
                        r2/=110;
                        r2/=DD[i];
                        if(U[i][k]*100%(110*DD[i])) r2++;

                        l=min(l1,l2);
                        r=max(r1,r2);

                        //cout<<i<<" "<<j<<" "<<k<<" "<<l1<<" "<<l2<<" "<<r1<<" "<<r2<<" "<<l<<" "<<r<<endl;

                        if(l<r) continue;

                        SetEdge(OUT((i-2)*p+j),IN((i-1)*p+k),1);
                    }
                }
            }
        }
        for(i=1;i<=p;i++)
        {
            SetEdge(OUT((n-1)*p+i),n*p*2+1,1);
        }

        for(i=1;i<=n;i++) for(j=1;j<=p;j++) SetEdge(IN((i-1)*p+j),OUT((i-1)*p+j),1);

        SRC=0;
        TNK=n*p*2+1;
        nV=TNK+1;

        ans=MaxFlow();
        printf("Case #%lld: %lld\n",cas,ans);

    }
}
