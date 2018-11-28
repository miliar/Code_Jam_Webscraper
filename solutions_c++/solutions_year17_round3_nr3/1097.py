#include <algorithm>
#include <iomanip>
#include <iostream>
#include <vector>

using namespace std;


double findAnswer(int n, int k, double u, vector<double>& prob)
{
    sort(prob.begin(), prob.end());

    // match as far as possible for k best cores
    for (int i = n - k + 1; i < n; ++i) {
        double match = prob[i];

        for (int j = n - k; j < i; ++j) {
            double parts = i - j;
            double delta = match - prob[j];
            
            if (delta * parts <= u) {
                prob[j] += delta;
                u -= delta;
            } else {
                double rest = u / parts;
                prob[j] += rest;
                u -= rest;
            }
        }

        if (u == 0.0) {
            break;
        }
    }

    // add the rest to k best cores
    double rest = min(u / k, 1.0 - prob[n - 1]);
    for (int i = n - k; i < n; ++i) {
        prob[i] += rest;
        u -= rest;
    }


    // match as far as possible for resting processes
    for (int i = 1; i < n - k; ++i) {
        double match = prob[i];

        for (int j = 0; j < i; ++j) {
            double parts = i - j;
            double delta = match - prob[j];
            
            if (delta * parts <= u) {
                prob[j] += delta;
                u -= delta;
            } else {
                double rest = u / parts;
                prob[j] += rest;
                u -= rest;
            }
        }

        if (u == 0.0) {
            break;
        }
    }

    // add the rest to n-k worst cores
    rest = min(u / (n - k), 1.0 - prob[0]);
    for (int i = 0; i < n - k; ++i) {
        prob[i] += rest;
        u -= rest;
    }


    // calculate probabilities
    double result = 1.0;
    for (auto p : prob) {
        result *= p;
    }

    return result;
}


int main(int argc, char* argv[])
{
    int t;
    cin >> t;
    cout << fixed << setprecision(6);

    int n;
    int k;
    for (int i = 1; i <= t; ++i) {
        double u;
        vector<double> p;
        cin >> n >> k >> u;

        for (int j = 0; j < n; ++j) {
            double x;
            cin >> x;
            p.push_back(x);
        }

        cout << "Case #" << i << ": " << findAnswer(n, k, u, p) << endl;
    }

    return 0;
}
