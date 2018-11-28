#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>

using namespace std;

class gap {
    public:
        long long int begin;
        long long int size;
        gap(long long int bn, long long int sz){
            begin = bn;
            size = sz;
        }
};

bool myfn(gap a, gap b) {
    if(a.size != b.size)
        return a.size<b.size;
    else
        return a.begin>b.begin;
}

int main()
{
    int t;
    long long int n, k, ans[2];

    cin>>t;
    for(int x=0; x<t; ++x){
        cin>>n>>k;
        vector <gap> gaps;
        vector<gap>::iterator it;
        gaps.push_back(gap(0,n));
        for(long long int i=0; i<k; ++i){
            it = max_element(gaps.begin(), gaps.end(), myfn);
            iter_swap(it, gaps.end() - 1);
            it = gaps.end() - 1;
            gap new1(it->begin,(it->size - 1)/2), new2(it->begin + (it->size+1)/2, it->size/2);
            gaps.pop_back();
            gaps.push_back(new1);
            gaps.push_back(new2);
        }
        ans[0] = max((gaps.end() - 1)->size, (gaps.end() - 2)->size);
        ans[1] = min((gaps.end() - 1)->size, (gaps.end() - 2)->size);
        cout<<"Case #"<<x+1<<": "<<ans[0]<<" "<<ans[1]<<endl;
    }
    return 0;
}
