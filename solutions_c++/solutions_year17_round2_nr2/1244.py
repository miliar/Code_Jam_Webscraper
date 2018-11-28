#include <bits/stdc++.h>
using namespace std;

int t,n,r,o,y,g,b,v;
bool flag;
char prev,first;

int main(){
    scanf("%d", &t);
    for (int i = 1; i <= t; i++){
        scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);
        flag = true;
        if (2*o > b) flag = false;
        if (2*g > r) flag = false;
        if (2*v > y) flag = false;
        if (r > y+b) flag = false;
        if (y > r+b) flag = false;
        if (b > r+y) flag = false;
        if (r > y and r > b) first = 'r';
        else if (b > y and b > r) first = 'b';
        else first = 'y';
        printf("Case #%d: ", i);
        if (flag == false) printf("IMPOSSIBLE\n");
        else {
            prev = 'a';
            while (n){
                n--;
                if (prev == 'r'){
                    if (b == 1 and y == 1){
                        if (first == 'b') {
                            prev = 'b';
                            cout<<"B";
                            b--;
                            continue;
                        } else {
                            prev = 'y';
                            cout <<"Y";
                            y--;
                            continue;
                        }
                    }
                    if (b > y){
                        prev = 'b';
                        cout<<"B";
                        b--;
                    } else{
                        prev = 'y';
                        cout << "Y";
                        y--;
                    }
                } else if (prev == 'b'){
                    if (r == 1 and y == 1){
                        if (first == 'r') {
                            prev = 'r';
                            cout<<"R";
                            r--;
                            continue;
                        } else {
                            prev = 'y';
                            cout <<"Y";
                            y--;
                            continue;
                        }
                    }
                    if (r > y){
                        prev = 'r';
                        cout<<"R";
                        r--;
                    } else{
                        prev = 'y';
                        cout << "Y";
                        y--;
                    }
                } else if (prev == 'y'){
                    if (r == 1 and b == 1){
                        if (first == 'r') {
                            prev = 'r';
                            cout<<"R";
                            r--;
                            continue;
                        } else {
                            prev = 'b';
                            cout <<"B";
                            b--;
                            continue;
                        }
                    }
                    if (b > r){
                        prev = 'b';
                        cout<<"B";
                        b--;
                    } else{
                        prev = 'r';
                        cout << "R";
                        r--;
                    }
                } else if (prev == 'a'){
                    if (b > r and b > y){
                        prev = 'b';
                        cout<<"B";
                        b--;
                    } else if (r > b and r > y){
                        prev = 'r';
                        cout <<"R";
                        r--;
                    } else {
                        prev = 'y';
                        cout <<"Y";
                        y--;
                    }
                }
            }
            cout<<endl;
        }
    }
}
