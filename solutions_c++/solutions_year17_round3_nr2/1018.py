#include <bits/stdc++.h>

using namespace std;


int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    cout.precision(20);
    for (int oo = 1; oo <= T; oo++){
        cout << "Case #" << oo << ": ";
     	int ac, aj;
     	cin >> ac >> aj;
     	int d[24*60];
     	for (int i=0;i<24*60;i++)
     		d[i] = 0;
     	int mc = -1;
     	int mq = -1;
     	for (int i = 0; i < ac; i++){
     		int x, y;
     		cin >> x >> y;
     		y--;
     		if ((x < mc) || (mc == -1))
     			mc = x;
     		if (y > mq)
     			mq = y;
     		for (int j = x; j <= y; j++)
     			d[j] = 1;
     	}
     	int mj = -1;
     	int mw = -1;
     	for (int i = 0; i < aj; i++){
     		int x, y;
     		cin >> x >> y;
     		y--;
     		if ((x < mj) || (mj == -1))
     			mj = x;
     		if (y > mw)
     			mw = y;
     		for (int j=x; j <= y; j++)
     			d[j] = 2;
     	}
     	bool f = false;
     	for (int i = 0; i < 24*60; i++){
     		bool ok = true;
     		for (int j = 0; j < 720; j++)
     			if (d[(i+j) % (24*60)] == 1)
     				ok = false;
     		for (int j = 0; j < 720; j++)
     			if (d[(i+j+720) % (24*60)] == 2)
     				ok = false;
     		if (ok){
     			f = true;
     			cout << 2 << endl;
     			break;
     		}
     	}
     	if (!f)
     		cout << 4 << endl;
    }   
    return 0;
}
