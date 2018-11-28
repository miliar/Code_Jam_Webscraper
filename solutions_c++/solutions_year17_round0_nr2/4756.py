#include <iostream>
#include <vector>

using namespace std;

typedef vector<unsigned short> digits;

bool tidy(size_t N, digits &ds, size_t &pos);
bool tidy(const digits &ds, size_t &pos);
digits to_digits(size_t N);
size_t from_digits(const digits &ds, size_t s = 0);

int main()
{
    unsigned short T = 0;
    cin >> T;
    for (unsigned short t = 1; t <= T; ++t)
    {
        size_t N, pos = 0;
        cin >> N;
        digits ds;
        while (!tidy(N, ds, pos))
            N -= from_digits(ds, pos) + 1;

        cout << "Case #" << t << ": " << N << '\n';
    }
}

digits to_digits(size_t N)
{
    digits ds;
    while (N)
    {
        ds.push_back(N % 10);
        N /= 10;
    }
    return ds; // NRVO should save me!
}

size_t from_digits(const digits &ds, size_t s)
{
    static const size_t pows10[] = {
        1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000,
        1000000000, 10000000000, 100000000000, 1000000000000,
        10000000000000, 100000000000000, 1000000000000000,
        10000000000000000, 100000000000000000, 1000000000000000000 };

    size_t N = 0;
    for (size_t i = 0; i < s; ++i)
        N += ds[i]*pows10[i];
    return N;
}

bool tidy(const digits &ds, size_t &pos)
{
    bool is_tidy = true;
    for (pos = ds.size() - 1; pos > 0 && is_tidy; --pos)
        is_tidy = is_tidy && (ds[pos] <= ds[pos-1]);
    return is_tidy;
}

bool tidy(size_t N, digits &ds, size_t &pos)
{
    ds = to_digits(N);
    return tidy(ds, pos);
}

