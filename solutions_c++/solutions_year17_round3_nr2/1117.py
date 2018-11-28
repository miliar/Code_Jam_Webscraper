#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    for (int ti=0; ti<t; ti++) {
        int ac, aj, a[110][2], b[110][2];
        cin >> ac >> aj;
        for (int i=0; i<ac; i++) {
            cin >> a[i][0] >> a[i][1];
        }
        for (int i=0; i<aj; i++) {
            cin >> b[i][0] >> b[i][1];
        }
        if (ac==0) {
            for (int i=0; i<aj; i++) {
                a[i][0] = b[i][0];
                a[i][1] = b[i][1];
            }
            ac = aj;
            aj = 0;
        }

        int ans_temp=0, ans=ac;
        for (int i=0; i<ac; i++) {
            ans_temp+=a[i][1]-a[i][0];
        }

        int temp;
        for (int i=0; i<ac; i++) {
            for (int j=0; j<i; j++) {
                if (a[j][0] > a[i][0]) {
                    temp = a[i][0]; a[i][0]=a[j][0]; a[j][0] = temp;
                    temp = a[i][1]; a[i][1]=a[j][1]; a[j][1] = temp;
                }
            }
        }

        int qn=0;
        int h[110];
        int flag;
        for (int i=0; i<ac-1; i++) {
            flag = 0;
            for (int j=0; j<aj; j++) {
                if (b[j][0] >= a[i][1] && b[j][1] <= a[i+1][0]) {
                    flag = 1;
                }
            }
            if (flag == 0) {
                h[qn] = a[i+1][0] - a[i][1];
                qn++;
            }
        }
        flag = 0;
        for (int j=0; j<aj; j++) {
            if (b[j][0] >= a[ac-1][1]) {
                flag = 1;
            }
            if (b[j][1] <= a[0][0]) {
                flag = 1;
            }
        }
        if (flag == 0) {
            h[qn] = 1440 + a[0][0] - a[ac-1][1];
            qn++;
        }

        for (int i=0; i<qn; i++) {
            for (int j=0; j<i; j++) {
                if (h[i] < h[j]) {
                    temp = h[i]; h[i]=h[j]; h[j]=temp;
                }
            }
        }
        // cout << ans_temp << " " << ans << endl;
        // cout << "ans_temp = " << ans_temp << endl;
        // for (int i=0; i<qn; i++) {
        //     cout << h[i] << " ";
        // }
        // cout << endl;
        int i=0;
        while (ans_temp+h[i] <= 720 && i<qn){
            ans--;
            ans_temp += h[i];
            i++;
        }
        cout << "Case #" << ti+1 << ": " << ans*2 << endl;
        // cout << endl;
    }
}
