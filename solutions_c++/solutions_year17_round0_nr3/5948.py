#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

int N[10002][3];

int Trova_max_sx(int sx) {
    int max = N[0][1];
    int ind = 0;
    for (int i = 1; i < sx; ++i)
        if (max < N[i][1]) {
            max = N[i][1];
            ind = i;
        }
    return ind;
}

int Trova_max_dx(int dx) {
    int max = N[0][2];
    int ind = 0;
    for (int i = 1; i < dx; ++i)
        if (max < N[i][2]) {
            max = N[i][2];
            ind = i;
        }
    return ind;
}

int Ordina(int kk) {
    bool scambio = false;
    int app, app_0, app_1, app_2;
    int i = 0;
    while (i < kk) {
        i++;
        if (N[i-1][0] > N[kk][0]) {
            app_0 = N[kk][0];
            app_1 = N[kk][1];
            app_2 = N[kk][2];
            N[kk][0] = N[i-1][0];
            N[kk][1] = N[i-1][1];
            N[kk][2] = N[i-1][2];
            N[i-1][0] = app_0;
            N[i-1][1] = app_1;
            N[i-1][2] = app_2;
            if (!scambio) {
                app = i - 1;
                scambio = true;
            }
        }
    }
    return app;
}

void Azzera_N(int kk) {
    for (int i = 0; i <= kk; ++i ) {
        N[i][0] = 0;
        N[i][1] = 0;
        N[i][2] = 0;
    }
}

int main() {
    int t_T;  // input = 1
    int n_N, k_K; // input per small e large
    int k;
    int max_sx, max_dx;
    int app;
    int k_app;
    int k_ord;

    cin >> t_T;
    for (int ie = 1; ie <= t_T; ++ie) {
        cin >> n_N >> k_K;

        Azzera_N(k_K);

        N[0][0] = 0;
        N[0][1] = 0;
        N[0][2] = n_N;
        N[1][0] = n_N + 1;
        N[1][1] = n_N;
        N[1][2] = 0;
        app = 0;
        k_app = 0;
        k_ord = 0;

        k = 2;
        while (k < k_K + 2) {
            max_sx = Trova_max_sx(k);
            max_dx = Trova_max_dx(k);

            if (N[max_dx][0] < N[max_sx][0] ) {
                app = N[max_sx][0] - N[max_dx][0] - 1;
                if (app % 2 == 0)
                    k_app = app / 2;
                else
                    k_app = (app / 2) + 1;
                k_app += N[max_dx][0];
                N[k][0] = k_app;
                N[k][1] = k_app - N[max_dx][0] - 1;
                N[k][2] = N[max_sx][0] - k_app - 1;

                N[max_dx][2] = N[k][1];
                N[max_sx][1] = N[k][2];
            }
            else {
                app = N[max_dx][0] - N[max_sx][0] - 1;
                if (app % 2 == 0)
                    k_app = app / 2;
                else
                    k_app = (app / 2) + 1;
                k_app += N[max_sx][0];
                N[k][0] = k_app;
                N[k][1] = k_app - N[max_sx][0] - 1;
                N[k][2] = N[max_dx][0] - k_app - 1;

                N[max_dx][1] = N[k][2];
                N[max_sx][2] = N[k][1];
            }

            k_ord = Ordina(k);
            k++;
        }

        cout << "Case #" << ie << ": " << N[k_ord][2] << " " << N[k_ord][1] << endl;

   }
   return 0;
}


