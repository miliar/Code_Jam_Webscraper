#include <iostream>
#define forn(i,j) for (int  x = i; x < j ; x++)
#define toInt(n) (n & 0xF)
#define toChar(n) (n +'0')

using namespace std;

typedef long long ll;

inline bool valid_number(string c){
    for (int  x = 0; x < c.length() -1; x++)
        if (toInt(c[x]) > toInt(c[x+1])) return false;
    return true;
}

inline string get_sol(string c){
    int u,d, aux;
    for (int  x = c.length() -1; x > 0; x--){
        u = toInt(c[x]);
        d = toInt(c[x-1]);
        if(u < d){
            c[x-1] = toChar( d -1);
            for (int  y = x; y < c.length(); y++){
                c[y] = '9';
            }
        }
    }
    if (c[0] == '0') return c.substr(1);
    return c;
}

int init(){
    int num_cases; 
    string c;
    cin >> num_cases;
     
    for (int  x = 1; x <= num_cases ; x++){
        cin >> c; 
        if (!valid_number(c)){
            cout << "Case #" << x << ": "<<get_sol(c) << endl;
        }else{
            cout << "Case #" << x << ": "<< c << endl;
        }
    }
    
}

int main(){
    init();
    return 0;
}
