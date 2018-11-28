#include <queue>
#include <set>
#include "iostream"


using namespace std;


struct Data{
    char pancake[1000];
    int cnt = 0;
    int filpSize;
};
int search(Data d);
bool noInminus(char *data);


int main() {

    int N;
    cin >> N;

    for (int i = 0; i < N; i++) {
        string data;
        int filpSize;
        cin >> data >> filpSize;
//        cout << data;

        const char * tmp = data.c_str();
//        char t[1000] = (char*) tmp;

        Data d;
        memcpy(d.pancake, tmp, 1000 );

        d.filpSize = filpSize;
        int result = search(d);
        if(result == -1)
            cout << "Case #" << i+1 << ": IMPOSSIBLE"<<endl;
        else
            cout << "Case #" << i+1 << ": "<< result <<endl;

    }
}

int search(Data d) {
    queue<Data> q;
    set<string> s;
    q.push(d);
    s.insert(string(d.pancake));
    while (!q.empty()) {
        Data p = q.front();
        q.pop();
        if(noInminus(p.pancake))
            return p.cnt;

        for(int sp = 0; sp < strlen(p.pancake) - p.filpSize + 1; sp++){
            Data p2;
            memcpy(&p2, &p, sizeof(struct Data));
            int ep = sp + p2.filpSize;
            for(int index = sp; index < ep; index++){
                if(p2.pancake[index] == '-')
                    p2.pancake[index] = '+';
                else
                    p2.pancake[index] = '-';
            }
            p2.cnt++;
            if(s.find(string(p2.pancake))!= s.end())
                continue;
            s.insert(string(p2.pancake));
            q.push(p2);
        }


    }
    return -1;
}

bool noInminus(char *d){
    for(int i=0; i< strlen(d); i++){
        if(d[i] == '-')
            return false;
    }
    return true;
}

