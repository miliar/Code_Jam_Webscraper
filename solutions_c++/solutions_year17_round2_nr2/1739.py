#include <iostream>
#include <queue>
#include <string>
#include <sstream>
#include <vector>
#include <map>
using namespace std;


void _main(){
	unsigned N, R, O, Y, G, B, V;

	cin >> N >> R >> O >> Y >> G >> B >> V;

    if(2*R > N || 2*O > N || 2*Y > N || 2*G > N || 2*B > N || 2*V > N){
        cout << "IMPOSSIBLE" << endl;
        return;
    }

    if(R < G || B < O || Y < V){
        cout << "IMPOSSIBLE" << endl;
        return;
    }

    char c0;
    if(R >= B && R >= Y){
        c0 = 'R';
        R--;
        cout << "R";
    } else if(B >= Y){
        c0 = 'B';
        B--;
        cout << "B";
    } else{
        c0 = 'Y';
        Y--;
        cout << "Y";
    }

    char c = c0;
    for(unsigned i=1; i<N-2; i++){
        if(c == 'R'){
            if(B >= Y){
                c = 'B';
                B--;
                cout << "B";
            } else{
                c = 'Y';
                Y--;
                cout << "Y";
            }
        } else if(c == 'B'){
            if(R >= Y){
                c = 'R';
                R--;
                cout << "R";
            } else{
                c = 'Y';
                Y--;
                cout << "Y";
            }
        } else{
            if(R >= B){
                c = 'R';
                R--;
                cout << "R";
            } else{
                c = 'B';
                B--;
                cout << "B";
            }
        }
    }

    if(c == 'R'){
        if(R != 0){
            if(B != 0)
                cout << "BR" << endl;
            else
                cout << "YR" << endl;
        } else if(c0 == 'B')
            cout << "BY" << endl;
        else
            cout << "YB" << endl;
    } else if(c == 'B'){
        if(B != 0){
            if(R != 0)
                cout << "RB" << endl;
            else
                cout << "YB" << endl;
        } else if(c0 == 'R')
            cout << "RY" << endl;
        else
            cout << "YR" << endl;
    } else{
        if(Y != 0){
            if(R != 0)
                cout << "RY" << endl;
            else
                cout << "BY" << endl;
        } else if(c0 == 'R')
            cout << "RB" << endl;
        else
            cout << "BR" << endl;
    }
}







int main(){
    unsigned caseNo;
    cin >> caseNo;

    for(unsigned i=1; i<=caseNo; i++){
		cout << "Case #" << i << ": ";
		_main();
    }
    return 0;
}








