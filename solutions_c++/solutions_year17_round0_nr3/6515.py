#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <fstream>
#include <set>
using namespace std;

int GetLS (string s, int i) {
    int j = (i-1);
    int cnt = 0;
    while (s[j] == '0') {
        cnt++;
        j--;
    }
    return cnt;
}

int GetRS (string s, int i) {
    int j = (i+1);
    int cnt = 0;
    while (s[j] == '0') {
        cnt++;
        j++;
    }
    return cnt;
}

struct segment {
    int l, u, s;
    bool operator< (const segment &other) const {
        if (s<other.s) {
            return false;
        } else if (s==other.s && (l+((u-l)/2))<(other.l+((other.u-other.l)/2))) {
            return false;
        }
        return true;
    }
};

int main () {
    ifstream fin ("bathroomSmallIN.txt");
    ofstream fout ("bathroomSmallOUT.txt");
    int T;
    fin >> T;
  //  cout << "\n\n";
    for (int t = 0; t < T; t++) {
        int N, K;
        fin >> N >> K;
        string s = "";
        s += "1";
        for (int i = 0; i < N; i++) {
            s += "0";
        }
        s += "1";
        int numPlaced = 0;
        int lower = 1, upper = N;
        set<segment> segments;
        segment ns;
        ns.l=lower;
        ns.u=upper;
        ns.s=ns.u-ns.l+1;
        segments.insert(ns);
        while (numPlaced < K) {
            segment seg = *(segments.begin());
            segments.erase(segments.begin());
            lower = seg.l;
            upper = seg.u;
            int segmentSize = seg.s;
          //  cout << "got " << lower << " " << upper << " " << segmentSize << "\n";
            //Where do we place this guy?
            int pickedVal;
            if (segmentSize <= 0)
                continue;
            pickedVal = lower + ((upper-lower)/2);
            s[pickedVal] = '1';
            numPlaced++;

            segment newSeg1;
            newSeg1.l=pickedVal+1;
            newSeg1.u=upper;
            newSeg1.s = newSeg1.u-newSeg1.l+1;
            segments.insert(newSeg1);
         //   cout << "pushed " << newSeg1.l << " " << newSeg1.u << " " << newSeg1.s << "\n";

            segment newSeg2;
            newSeg2.l=lower;
            newSeg2.u=pickedVal-1;
            newSeg2.s = newSeg2.u-newSeg2.l+1;
            segments.insert(newSeg2);
            //cout << "pushed " << newSeg2.l << " " << newSeg2.u << " " << newSeg2.s << "\n";

           // cout << "new s = \n" << s << "\n";
           // cout << "numPlaced = " << numPlaced << "\n\n\n";

          //  cout << "SEG SET:\n";
         //   for (auto it : segments) {
          //      cout << it.l << " " << it.u << " " << it.s << "\n";
          // }
           // cout << "\n\n";

            if (numPlaced == K) {
                int tls = GetLS(s,pickedVal);
                int trs = GetRS(s,pickedVal);
             //   cout << "final s = \n" << s << "\n";
                fout << "Case #" << (t+1) << ": " << max(tls,trs) << " " << min(tls,trs) << "\n";
            }
        }
    }

    return 0;
}
