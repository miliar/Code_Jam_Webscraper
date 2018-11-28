#include <bits/stdc++.h>
using namespace std;

struct comp//construct
{
    bool operator()(const pair<int, pair<int, int> >& a,const pair<int, pair<int, int> >& b)
    {
        if (a.first == b.first)
            return a.second > b.second;
        return (a.first<b.first);
    }
};



int main() {

    ifstream infile;
    ofstream outfile;
    infile.open("C-small-2-attempt0.in");
    outfile.open("out.txt");

    int t;
    infile>>t;
    for(int cas =1;cas<=t;cas++)
    {
        int n,k;
        infile>>n>>k;
        priority_queue< pair<int, pair<int, int> > , vector<pair<int, pair<int, int> > >,comp > q;
        pair<int, pair<int, int> > res;
        q.push(make_pair(n+1, make_pair(0,n+1)));
        while(k--)
        {
            res = q.top();
            q.pop();
            pair<int, pair<int, int> > tmp,tmp2;
            int beg,mid,end;
            beg = res.second.first;
            end= res.second.second;
            mid = (beg+end)/2;
            tmp.second.first = beg;
            tmp.second.second = mid;
            tmp2.second.first = mid;
            tmp2.second.second = end;
            tmp.first = tmp.second.second- tmp.second.first;
            tmp2.first = tmp2.second.second- tmp2.second.first;
            q.push(tmp);
            q.push(tmp2);

        }
        int beg,mid,end;
        beg = res.second.first;
        end= res.second.second;
        mid = (beg+end)/2;
        cout<<"("<<beg<<" "<<mid<<" "<<end<<")"<<"   ANS:  "<<max(mid-beg,end-mid)-1<<" "<<min(mid-beg,end-mid)-1;
        outfile<<"Case #"<<cas<<": "<<max(mid-beg,end-mid)-1<<" "<<min(mid-beg,end-mid)-1<<endl;
    }
    return 0;
}

