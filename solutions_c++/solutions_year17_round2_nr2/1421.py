#include <bits/stdc++.h>
using namespace std;

long long arr[10000], colors[7];

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	long long T, cas, N, i, a, b, c, j;
	string names[3] = {"R", "Y", "B"};
	cin >> T;
	for(cas=1;cas<=T;cas++){
	    cout << "Case #" << cas << ": ";
        cin >> N;
        names[0] = "R";
        names[1] = "Y";
        names[2] = "B";
        for(i=0;i<6;i++) cin >> colors[i];
        for(i=0;i<N;i++) arr[i] = 0;
        a = colors[0];
        b = colors[2];
        c = colors[4];
        if(b>a){
            swap(a, b);
            swap(names[0], names[1]);
        }
        if(c>a){
            swap(a, c);
            swap(names[0], names[2]);
        }
        if(c>b){
            swap(b, c);
            swap(names[1], names[2]);
        }
        //cout << a << " " << b << " " << c << names[0] << names[1] << names[2] << '\n';
        for(i=0;i<N and a;i+=2){
            arr[i] = 1;
            //cout << "** " << names[0] << " " << i << '\n';
            a--;
        }
        if(a or arr[0]==arr[N-1]){
            cout << "IMPOSSIBLE\n";
            continue;
        }
        i--;
        j = i-2;
        for(;i<N and b;i+=2){
            arr[i] = 2;
             //cout << "** " << names[1] << " " << i << '\n';
            b--;
        }
        for(i=j;i>=0 and b;i-=2){
            arr[i] = 2;
            //cout << "** " << names[1] << " " << i << '\n';
            b--;
        }
        if(b){
            cout << "IMPOSSIBLE\n";
            continue;
        }
        else{
            for(i=0;i<N;i++){
                if(arr[i]==0) arr[i] = 3;
            }
            for(i=0;i<N;i++){
                cout << names[arr[i]-1];
            }
            cout << '\n';
        }
	}
	return 0;
}
