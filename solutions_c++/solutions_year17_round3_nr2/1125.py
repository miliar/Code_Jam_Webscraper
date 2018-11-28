#include <bits/stdc++.h>
using namespace std;
int main(){
    ifstream infile;
    ofstream outfile;
    long long t;
    infile.open("B-small-attempt0.in");
    outfile.open("B-output.out");
    infile>>t;
    for(long long tk=1;tk<=t;tk++){
        long c,j;
        infile>>c>>j;
        vector<pair<long long, long long> > cam(c), jai(j);
        for(long i=0;i<c;i++)
            infile>> cam[i].first>> cam[i].second;
        for(long i=0;i<j;i++)
            infile>> jai[i].first>> jai[i].second;
        long long ans = 0;
        if(c <= 1 && j <= 1)
            ans = 2;
        else {
            vector<pair<long long, long long> > arr;
            if(c == 0)
                arr = jai;
            else arr = cam;
            sort(arr.begin(),arr.end());
            long long outd = arr[0].first + 1440 - arr[1].second;
            long long ind = arr[1].first -arr[0].second;
            if(outd >= 720 || ind >= 720)
                ans = 2;
            else
                ans = 4;
        }

        outfile<<"Case #"<<tk<<": "<<ans;
        outfile<<endl;
    }
    infile.close();
    outfile.close();
    return 0;
}
