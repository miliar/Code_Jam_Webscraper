#include <iostream>
#include <string>
#include <fstream>
#include <vector>


using namespace std;

struct dist {
    dist(int d1 = -1, int d2 = -1):min_dist(d1), max_dist(d2){}
    int min_dist;
    int max_dist;
};

int getSl (const vector<int>& array, int idx)
{
    int sl = 0;
    for (int i = idx-1; i >= 0; --i) {
        if (array[i] == 0){
            ++sl;
        } else {
            break;
        }
    }
    return sl;
}

int getSr (const vector<int>& array, int idx)
{
    int sr = 0;
    for (int i = idx+1; i < array.size(); ++i) {
        if (array[i] == 0) {
            ++sr;
        } else {
            break;
        }
    }
    return sr;
}

dist take(vector<int>& array)
{
    dist d;
    int taken = -1;
    for (int i = 1; i < array.size() -1; ++i) {
        if (array[i] == 0) {
            int sl = getSl(array, i);
            int sr = getSr(array, i);
            //cout << sl << " " << sr << endl;

            int min_dist = min(sl, sr);
            int max_dist = max(sl, sr);


            if (min_dist > d.min_dist) {
                d = dist(min_dist, max_dist);
                taken = i;
            } else if (min_dist == d.min_dist && max_dist > d.max_dist) {
                d = dist(min_dist, max_dist);
                taken = i;
            }
        }
    }
    //cout << taken << endl;

    array[taken] = 1;

    return d;
}

dist solve(int N, int K)
{
    vector<int> array;
    array.resize(N+2);
    for (int i = 0; i < array.size(); ++i) {
        array[i] = 0;
    }

    array[0] = array[N+1] = 1;

    dist result;
    for (int i = 0; i < K; ++i) {
        result = take(array);
    }

    return result;
}

int main()
{
    int T, N, K;

    ifstream fin("input.txt");
    ofstream fout("output.txt");

    fin >> T;
    for (int i = 0; i < T; ++i) {
        fin >> N >> K;
        fout << "Case #" << i+1 <<": ";
        dist result = solve(N, K);
        fout << result.max_dist<<" "<<result.min_dist << endl;
    }



    return 0;
}

