#include <bits/stdc++.h>

using namespace std;

int main()
{
    //freopen("C-small-2-attempt0.in", "r", stdin);
    //freopen("C-small-2-attempt0.out", "w", stdout);

    int T;
    long long N, K;
    long long soDua, doDai, soKhuc, maxLengthFinal, leftS, rightS;

    long long number, temp;

    long long khucLon, khucBe, soLuongKhucLon, soDuaConLai;

    cin >> T;
    for(int i = 0; i < T; i++){
        cin >> N >> K;


        number = (long long) log2(K);
        temp = pow(2, number);

        soDua = temp - 1;

        if(soDua == 0){
            maxLengthFinal = N;
        } else {
            doDai = N - soDua;

            soKhuc = soDua + 1;

            khucLon = doDai/soKhuc + (doDai%soKhuc != 0);
            khucBe = doDai/soKhuc;

            soLuongKhucLon = doDai%soKhuc;
            soDuaConLai = K - soDua;

            if(soDuaConLai <= soLuongKhucLon){
                maxLengthFinal = khucLon;
            } else {
                maxLengthFinal = khucBe;
            }
        }

        if(maxLengthFinal %2 == 0){
            leftS = maxLengthFinal/2 - 1;
            rightS = maxLengthFinal/2;
        } else {
            leftS = maxLengthFinal/2;
            rightS = maxLengthFinal/2;
        }
        cout << "Case #" << i+1 << ": " << rightS << " " << leftS << endl;
    }

    return 0;
}
