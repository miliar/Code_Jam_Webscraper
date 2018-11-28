#include <iostream>
#include <set>
#include <cstdlib>
#include <stdexcept>
#include <cassert>
#include <string>
#include <cstdio>
#include <cstring>
#include <string>

typedef long long lint;
using namespace std;

class node{
public:
    lint LEN,NUM;
    node(){
        LEN=NUM=0;
    }
    node(lint LENx, lint NUMX){
        LEN=LENx;
        NUM=NUMX;
    }
};

pair<lint, lint> countans(lint x){
    return make_pair(x/2, (x-1)/2);
}

void addto(node& cn1, node& cn2, node sta){
    if (cn1.LEN == sta.LEN){
        cn1.NUM += sta.NUM;
        return;
    }
    if (cn2.LEN == sta.LEN){
        cn2.NUM += sta.NUM;
        return;
    }
    if (cn2.LEN == 0)
        cn2 = sta;
}

pair<lint, lint> getans(node n1, node n2, lint k){
    if (n1.LEN < n2.LEN)
        swap(n1, n2);
    if (n1.NUM+n2.NUM >= k)
        return n1.NUM>=k ? countans(n1.LEN) : countans(n2.LEN);
    node cn1,cn2;
    if (n1.LEN%2 == 1)
        cn1 = node(n1.LEN/2, n1.NUM*2);
    else {
        cn1 = node(n1.LEN/2, n1.NUM);
        cn2 = node((n1.LEN-1)/2, n1.NUM);
    }

    if (n2.LEN%2 == 1){
        addto(cn1, cn2, node(n2.LEN/2, n2.NUM*2));
    } else {
        addto(cn1, cn2, node(n2.LEN/2, n2.NUM));
        addto(cn1, cn2, node(n2.LEN/2-1, n2.NUM));
    }
    return getans(cn1, cn2, k-n1.NUM-n2.NUM);
}

int main(){
    freopen("data.in", "r", stdin);
    freopen("data.txt", "w", stdout);

    lint T,k,cas,n;
    cin>>T;
    for (cas=1; cas<=T; cas++){
        cin>>n>>k;
        pair<lint, lint> ans_pair = getans(node(n,1), node(), k);
        cout<<"Case #"<<cas<<": ";
        cout<<ans_pair.first<<' '<<ans_pair.second<<endl;
    }
    return 0;
}
