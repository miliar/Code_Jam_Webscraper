#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

bool checkKit(int n){
	int a,b;
	while (n>0){
		a = n%10;
		n = n/10;
		b = n%10;
		if (a<b) 
			return false;
	}
	return true;
}

int main(){
	ofstream myfile;
  	myfile.open ("out2.txt");
    int q[3][10], r[10], q0[10], q1[10];
  	int rn, n, p, res, t;
    int i, j, tmin, tmax;
  	cin >> rn;
  	for (int ri=0; ri<rn; ri++){
  		cin >> n >> p;
  		for (int i=0; i<n; i++)
            cin >> r[i];
        for (int i=0; i<n; i++)
        for (int j=0; j<p; j++)
            cin >> q[i][j];

        res = 0;
        if (n==1)
        for (int i=0; i<p; i++){
            t = (int)(q[0][i]/(r[0]*0.9));
            if (t>=q[0][i]/(r[0]*1.1)){
                res ++;
            }
        }

        if (n==2){
            for (int i=0; i<p; i++){
                q0[i] = q[0][i];
                q1[i] = q[1][i];
            }
            sort(q0, q0+p);
            sort(q1, q1+p);

            i = j = 0;
            while ((i<p)&&(j<p)){
                tmax = (int)(q0[i]/(r[0]*0.9));
                tmin = (int)(q0[i]/(r[0]*1.1));
                if (q0[i]/(r[0]*1.1)-tmin>0.00001)
                    tmin++;
                //cout << tmin << " " << tmax << endl;
                while ((q1[j]<tmin*r[1]*0.9)&&(j<p)) j++;
                //cout << q1[j] <<endl;
                if (j<p)
                for (int k=tmin; k<=tmax; k++)
                    if ((q1[j]>=k*r[1]*0.9)&&(q1[j]<=k*r[1]*1.1)){
                        //cout << q1[j] << endl;
                        res++;
                        j++;
                        break;
                    }
                i++;
            }
        }
        cout << "here" << endl;

  		myfile << "Case #" << ri+1 << ": " << res << endl;
  	}
  	myfile.close();
  	return 0;
}