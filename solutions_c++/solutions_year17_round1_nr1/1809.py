#include <iostream>

using namespace std;

void fill(string& s,int b,int e,char c) {
    while(b<=e)
	s[b++]=c;
}
bool span_free(string& s,int b,int e) {
    while(b<=e)
	if(s[b++]!='?')
	    return false;
    return true;
}

void test(int cse)
{
    cout<<"Case #"<<cse<<": "<<endl;
    int R,C; cin>>R>>C;
    string cake[R];
    for(int i=0; i<R; i++)
	cin>>cake[i];

    bool g[256]={false};
    g['?']=true;
    for(int i=0; i<R; i++) {
	for(int j=0; j<C; j++) {
	    char x=cake[i][j];
	    if(g[x])
		continue;
	    g[x]=true;
	    // grow piece
	    int w1=j,w2=j;
	    while(w1>0 && cake[i][w1-1]=='?')
		w1--;
	    while(w2<C-1 && cake[i][w2+1]=='?')
		w2++;
	    fill(cake[i],w1,w2,x);
	    int h1=i,h2=i;
	    while(h1>0 && span_free(cake[h1-1],w1,w2))
		fill(cake[--h1],w1,w2,x);
	    while(h2<R-1 && span_free(cake[h2+1],w1,w2))
		fill(cake[++h2],w1,w2,x);
	}
    }


    for(int i=0; i<R; i++)
	cout<<cake[i]<<endl;
}

int main()
{
    int T; cin>>T;
    for(int i=1; i<=T; i++)
	test(i);
    return 0;
}
