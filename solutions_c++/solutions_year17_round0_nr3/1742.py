#include <iostream>
#include <cassert>

using namespace std;

typedef unsigned long long ull;
typedef pair<ull,ull> mm;

mm find_mm(ull N,ull K)
{
    assert(N>=K);
    if(N==K)
	return make_pair(0ULL,0ULL);
    if(K==1)
	return make_pair(N/2,(N-1)/2);

    if(K&1)
	return find_mm((N-1)/2,(K-1)/2);
    return find_mm(N/2,K/2);
}

void test(int cse)
{
    cout<<"Case #"<<cse<<": ";
    ull N,K; cin>>N>>K;
    mm x=find_mm(N,K);
    cout<<x.first<<' '<<x.second<<endl;
}

int main()
{
    int T; cin>>T;
    for(int i=1; i<=T; i++)
	test(i);
    return 0;
}
