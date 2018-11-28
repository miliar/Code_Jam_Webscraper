#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// uint32_t left(uint64_t value) {
//   return value >> 4;
// }
//
// uint32_t right(uint64_t value) {
//   return value & 0xFFFF;
// }
//
// uint64_t set(uint64_t value) {
//   uint32_t l = value >> 2;
//   uint32_t r = value - l;
//   return set(v, right);
// }
// uint64_t set(uint32_t left, uint32_t right) {
//   uint64_t v = left;
//   v << 4;
//   v & right;
//   return v;
// }
//
// uint32_t min(uint64_t v) {
//   return std::min(left(v), right(v))
// }
//
// uint32_t max(uint64_t v) {
//   return std::max(left(v), right(v))
// }

struct Occupation
{
    Occupation(uint64_t v) : occupied(false)
    {
        if (v % 2 > 0) {
            left = (v / 2);
            right = v - left - 1;
        } else {
            left = (v / 2);
            right = v - left;
            if (left != 0) {
                left -= 1;
            }
        }

      //  cout << "L: " << left << " R: " << right << endl;
    }

    uint64_t left;
    uint64_t right;
    bool occupied;
};

std::vector<Occupation> generateOccupation(const std::vector<Occupation>& o, int index)
{
    std::vector<Occupation> result;
    for (int i = 0; i < index; ++i) {
        auto parent = o.at(i);
        result.push_back(Occupation(parent.left));
        result.push_back(Occupation(parent.right));
    }

    std::sort(result.begin(), result.end(), [](const Occupation& l, const Occupation& r) {

        if (std::min(r.left, r.right) < std::min(l.left, l.right)) {
            return true;
        } else {
            return std::max(r.left, r.right) < std::max(l.left, l.right);
        }
    });

    return result;
}

void calculate(uint64_t people, uint64_t stalls, uint64_t * x, uint64_t * y)
{
//    cout << "P: " << people << " S: " << stalls << endl;

    int index = 0;
    std::vector<Occupation> occupation(1, Occupation(stalls));

    for (uint64_t i = 0; i < people; ++i) {
        if (index >= occupation.size()) {
            // Create new leaves
            occupation = generateOccupation(occupation, index);
            index = 0;
        }

        ++index;
    }

    // Last increase will be removed
    --index;

    if (index < occupation.size()) {
        auto o = occupation.at(index);
        *x = std::max(o.left, o.right);
        *y = std::min(o.left, o.right);
    }
}

int main() {
    int t;
    uint64_t k, n, x, y;

    cin >> t;

    for (int i = 1; i <= t; ++i) {
        cin >> n >> k;
        calculate(k, n, &x, &y);
        cout << "Case #" << i << ": " << x << " " << y << endl;
    }
    return 0;
}
