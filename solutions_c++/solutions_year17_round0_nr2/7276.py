#include <bits/stdc++.h>



using namespace std;

int t;
long long n;
deque <int> c;

int main() {
    ifstream in("file.in");
    ofstream out("file.out");
    in >> t;
    for(int h=1;h<=t;h++){
        in >> n;
        c.clear();
        while(n){
            c.push_front(n%10);
            n/=10;
        }
        int p=0;
        while(p<c.size()-1 && c[p]<=c[p+1]) p++;
        if(p==c.size()-1){
            out << "Case #" << h << ": ";
            for(int i=0;i<c.size();i++){
                out << c[i];
            }
            out << '\n';
            continue;
        }
        while(p && c[p]==c[p-1]) p--;
        c[p]--;
        for(int i=p+1;i<c.size();i++) c[i]=9;
        out << "Case #" << h << ": ";
        for(int i=0;i<c.size();i++){
            if(!i && !c[i]) continue;
            out << c[i];
        }
        out << '\n';
    }
}
