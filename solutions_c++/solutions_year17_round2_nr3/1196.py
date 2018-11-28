#include <bits/stdc++.h>

#define fi first
#define se second

using namespace std;

typedef pair <int,int> ii;
int T,N,Q;
ii ar[110];
vector <ii> v[110];

struct node{
	int distleft,speed,where;
	double timepassed;
	node( int a , int b , int x , double d ){
		distleft=a; speed=b; where=x; timepassed=d;
	}
	friend bool operator < ( const node &a , const node &b ){
		return a.timepassed > b.timepassed;
	}
};

priority_queue <node> q;

int main(){
	
	cin >> T;
	
	for( int mask=1 ; mask<=T ; mask++ ){
		cin >> N >> Q;
		for( int i=1 ; i<=N ; i++ ) v[i].clear();
		for( int i=1 ; i<=N ; i++ )	scanf(" %d %d",&ar[i].fi , &ar[i].se );
		for( int i=1 ; i<=N ; i++ )
			for( int j=1,a ; j<=N ; j++ ){
				scanf(" %d",&a);
				if( a != -1 ) v[i].push_back( ii( a , j ) );
			}
		printf("Case #%d:",mask);
		int from,towhere;
		while( Q-- ){
			while( !q.empty() ) q.pop(); 
			scanf(" %d %d",&from,&towhere);
			q.push( node( 0 , 0 , from , 0 ) );
			while( true ){
				node current=q.top();
				q.pop();
				if( current.where == towhere ){
					printf(" %lf",current.timepassed);
					break;
				}
				for( int i=0 ; i<(int)v[current.where].size() ; i++ )
					if( current.distleft >= v[current.where][i].fi )
						q.push( node( current.distleft-v[current.where][i].fi , current.speed , v[current.where][i].se , current.timepassed+(double)v[current.where][i].fi/current.speed ));
				current.distleft=ar[current.where].fi;
				current.speed=ar[current.where].se;
				for( int i=0 ; i<(int)v[current.where].size() ; i++ )
					if( current.distleft >= v[current.where][i].fi )
						q.push( node( current.distleft-v[current.where][i].fi , current.speed , v[current.where][i].se , current.timepassed+(double)v[current.where][i].fi/current.speed ));
			}
		}
		puts("");
	}
	
	return 0;
}
