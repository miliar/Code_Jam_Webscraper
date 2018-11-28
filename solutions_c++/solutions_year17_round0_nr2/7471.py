#include <iostream>

using namespace std;


int T;
int N;
bool f[1007];


int main(){
    

    for(int i = 1; i < 1001; i++){
        int n = i;
        int d = n%10;
        n = n/10;
        int c = n%10;
        n = n/10;
        int b = n%10;
        n = n/10;
        int a = n%10;
        if(a <= b &&  b <= c && c <= d){
            f[i]=true;
        }
    }

    cin >> T;
    for(int t = 1; t <= T; t++){
        cin >> N;
        int answer = 0;
        while(answer == 0){
            if(f[N]){
                answer = N;
            }
            N--;
        }
        cout << "Case #" << t << ": " << answer << endl;

    }






    return 0;
}
