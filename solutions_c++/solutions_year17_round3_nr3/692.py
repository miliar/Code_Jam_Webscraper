# include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("C-small-1-attempt0.in", "r", stdin);
    freopen("C-small-out.txt", "w", stdout);
    int cases, caseno=0, n, k;
    double probability, x, ans, eps = 1e-12;
    vector <double> prob;
    cin >> cases;
    while(cases--){
        cin >> n >> k;
        cin >> x;
        prob.clear();
        for (int i=0; i<n; i++){
            cin >> probability;
            prob.push_back(probability);
        }
        sort(prob.begin(), prob.end());
        for (int i=0; i<n-1 && x > eps; i++){
            probability = prob[i+1]-prob[i];
            if (probability > eps){
                probability = min(probability, x/(i+1));
                //cout << i << " " << prob[i] << " " << x << endl;
                x -= probability*(i+1);
                //cout << "X is now " << x << "\nIn inner loop" << endl;
                for (int j=0; j<=i; j++){
                    prob[j] += probability;
                    //cout << j << " " << prob[j] << " " << endl;
                }
            }
        }
        //cout << "Out of loops\n";
        if (x>eps){
            probability = x/n;
            for (int j=0; j<n; j++){
                prob[j] += probability;
                //cout << j << " " << prob[j] << endl;
            }
        }
        ans = 1;
        for (int j=0; j<n; j++){
            ans *= prob[j];
        }
        printf("Case #%d: %0.8lf\n", ++caseno, ans);
    }
    return 0;
}

