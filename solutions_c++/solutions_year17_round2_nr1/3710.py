#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

struct Horse
{
    double K;
    double S;
    
    Horse()
    {
        cin >> K >> S;
    }
    
    double timeToReach(double D)
    {
        double remainingDistance = D - K;
        if (remainingDistance > 0)
        {
            double result = remainingDistance/S;
            return result;
        }
        return 0;
    }
};

struct Functor
{
    double D;
    Functor(double Din)
    {
        D = Din;
    }
    bool operator()(Horse &h1, Horse &h2)
    {
        return (h1.timeToReach(D) < h2.timeToReach(D));
    }
};

void solve(unsigned int testCase);

int main()
{
    cout << fixed << setprecision(6);
    unsigned int T;
    cin >> T;
    
    for (unsigned int i = 0; i < T; ++i)
        solve(i+1);
}

void solve(unsigned int testCase)
{
    cout << "Case #" << testCase << ": ";
    
    double D, N;
    cin >> D >> N;
    vector<Horse> horses(N);
    
    Functor compare(D);
    sort(horses.begin(), horses.end(), compare);
    
    double result = D/(horses.back().timeToReach(D));
    cout << result << '\n';
    
}

//first calc the time itll take each horse to reach the destination
