#include <iostream>

using namespace std;

int bad(char a, char b){
	if (a==b)return 1;
	return 0;
}

int main(){
	int t;
	cin >> t;
	int C=1;
	while (C<=t){
		int n;
		int r,o,y,g,v,b;
		cin >> n >> r >> o >> y >> g >> b >> v;

		int degr,dego,degy,degg,degv,degb;
		degr = y+b+g;
		degy = r+b+v;
		degb = r+y+o;
		dego = n-(r+y);
		degg = n-(y+b);
		degv = n-(r+b);

		int a[6],d[6];
		char c[6];
		a[0] = r;
		a[1] = o;
		a[2] = y;
		a[3] = g;
		a[4] = v;
		a[5] = b;
		d[0] = degr;
		d[1] = dego;
		d[2] = degy;
		d[3] = degg;
		d[4] = degv;
		d[5] = degb;
		c[0] = 'R';
		c[1] = 'O';
		c[2] = 'Y';
		c[3] = 'G';
		c[4] = 'V';
		c[5] = 'B';


		cout << "Case #" << C << ": ";
		C++;
		int flag = 0;
		for (int i=0;i<6;i++){
			if (a[i]!=0 && (2*d[i]<n)){
				cout << "IMPOSSIBLE\n";
				flag = 1;
				break;
			}
		}

		if (flag)continue;

		char arr[2*n];
		int pos = 0;
		for (int i=0;i<6;i++){
			for (int j=0;j<a[i];j++){
				arr[pos++] = c[i];
			}
		}
		for (int i=0;i<n;i++){
			arr[i+n] = arr[i];
		}
		flag = 1;
		while (flag){

			flag = 0;
			for (int i=0;i<n;i++){
				if (bad(arr[i],arr[i+1])){
					for (int jj=1;jj<n;jj++){
						int j = jj+i;
						if ((!bad(arr[i],arr[j])) && (!bad(arr[i+1],arr[(j+1)]))){
							reverse(arr+i+1,arr+j+1);
							for (int ind=0;ind<2*n;ind++){
								if (ind>i && ind<j+1){
									// This was changed
									if (ind<n)arr[n+ind] = arr[ind];
									else arr[ind-n] = arr[ind];
								}
							}
							flag = 1;
							break;
						}
						if (flag)break;
					}
				}
			}
		}

		for (int i=0;i<n;i++){
			cout << arr[i];
		}
		cout << endl;

	}

}