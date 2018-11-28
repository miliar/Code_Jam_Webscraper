#include<bits/stdc++.h>
using namespace std;

int N, K, T;
int last;
int izq = 0, der = 0;
vector<int> bath;

void finish(int s){
    izq = 0; der=0;
    for(int j=s-1; bath[j] == 0; j--){
        if(bath[j] == 0) {
            izq++;
        }
    }

    for(int j=s+1; bath[j] == 0; j++){
        if(bath[j] == 0) {
            der++;
        }
    }
}

struct Stall{
    int size;
    int L, R;
};

typedef bool (*comp)(Stall,Stall);

bool compare(Stall a, Stall b)
{
   if (a.size != b.size){
        return a.size<b.size;
   } else {
        return a.L > b.L;
   }
}

vector<Stall> stalls;


void calc(){
    bath.clear();
    bath.resize(N+4);
    bath[0] = -1;
    bath[N+1] = -1;
    priority_queue<Stall, vector<Stall>, comp> cola(compare);
    Stall s;
    s.size = N; s.L = 1; s.R = N;
    cola.push(s);
    for(int i=1; i<=K; i++){
        int left = cola.top().L;
        int right = cola.top().R;
        cola.pop();
        if(left == right){
            bath[left] = i;
            last = left;
            continue;
        }
        int mid = (right+left)/2;
        bath[mid] = i;
        last = mid;
        s.size = mid-left;
        s.L = left;
        s.R = mid-1;
        cola.push(s);
        s.size = right - mid;
        s.L = mid+1;
        s.R = right;
        cola.push(s);
    }

}

int main() {

    ifstream cin("C-small-2-attempt0.in");
    ofstream cout("C-output-med.txt");

    cin >> T;
    for(int t=1; t<=T; t++){
        cin >> N >> K;
        calc();
        finish(last);
        cout << "Case #" << t << ": " << max(izq, der) << " " << min(izq, der) << endl;

    }
}

