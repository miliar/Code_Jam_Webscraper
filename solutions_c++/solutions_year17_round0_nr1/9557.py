#include <iostream>
#include <string>

using namespace std;

class Pancakes
{
  private:
    string _S;
    int _K;

    void oversizedFlip(int startPosition)
    {
        for (int i = 0; i < _K; i++)
        {
            singleFlip(startPosition + i);
        }
    }

    void singleFlip(int position)
    {
        _S[position] = _S[position] == '-' ? '+' : '-';
    }

    bool allPancakesHappy()
    {
        for (int i = _S.length() - _K; i < _S.length(); i++)
        {
            if (_S[i] != '+')
            {
                return false;
            }
        }

        return true;
    }

  public:
    Pancakes(string S, int K) : _S(S), _K(K) {}
    int minNumberOfFlips()
    {
        int numberOfFlips = 0;

        for (int i = 0; i < _S.length() - _K + 1; i++)
        {
            if (_S[i] == '-')
            {
                numberOfFlips++;
                oversizedFlip(i);
            }
        }

        return allPancakesHappy() ? numberOfFlips : -1;
    }
};

int main()
{
    int T;
    string S;
    int K;
    cin >> T;

    for (int testCase = 0; testCase < T; testCase++)
    {
        cin >> S >> K;
        Pancakes pancakes(S, K);
        int minFlips = pancakes.minNumberOfFlips();

        cout << "Case #" << testCase + 1 << ": ";
        string output = minFlips == -1 ? "IMPOSSIBLE" : to_string(minFlips);
        cout << output << endl;
    }

    return 0;
}
