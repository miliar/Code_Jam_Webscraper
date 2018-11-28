#include <iostream>
#include <vector>
#include <algorithm>

std::vector<long long>from_number_to_array(long long n) {
    long long power = 1;
    long long m = n;
    std::vector<long long> result;
    while (power <= n) {
        result.push_back(m % 10);
        m  = m / 10;
        power *= 10;
    }

    std::reverse(result.begin(), result.end());
    return result;
}

long long from_array_to_number(std::vector<long long>& input) {
    long long result = 0;
    for (size_t i = 0;  i < input.size(); i++) {
        result = result * 10;
        result += input[i];
    }
    return result;
}

long long min_val(int current_id, std::vector<long long>& input) {
    long long ans = 0;

    for (size_t i = 0; i <= current_id; i++) {
        ans *= 10;
        ans += input[i];

    }
    for (size_t i = current_id + 1; i < input.size(); i++) {
        ans *= 10;
        ans += input[current_id];
    }
    return ans;
}
long long max_val(int current_id, std::vector<long long>& input) {
    long long ans = 0;
    for (size_t i = 0; i <= current_id; i++) {
        ans *= 10;
        ans += input[i];
    }
    for (size_t i = current_id+1; i < input.size(); i++) {
        ans *= 10;
        ans += 9;
    }
    return ans;
}

long long max_value(long long n) {
    if (n <= 10) {
        return n;
    }
    std::vector<long long> arr = from_number_to_array(n);
    long long current_max = 0;
    for (size_t i = 0; i < arr.size() - 1; i++) {
        current_max *= 10;
        current_max += 9;
    }

    int current_id = 0;
    std::vector<long long> answer = std::vector<long long>(arr.size(), 1);

    while (current_id < arr.size()) {
        long long min_v = min_val(current_id, answer);
        long long max_v = max_val(current_id, answer);
//        std::cout << min_v <<" " << max_v<< " "<< current_max<<" "<< current_id<< " " << from_array_to_number(answer) << std::endl;
        if (n > max_v) {
            //modify current max
            current_max = max_v;
            answer[current_id] += 1;
        } else if (min_v < n && n < max_v) {
            //increment_id
            current_id++;;
        } else if (max_v == n) {
            return max_v;
        } else if (min_v == n) {
            return min_v;
        } else if (n < min_v ) {
          return current_max;
        }
    }
    return from_array_to_number(answer);
}


int main(int argc, char *argv[])
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int test_case_number;
    scanf("%d", &test_case_number);
    for (int i = 1; i <= test_case_number; i++) {
        long long  n;
        scanf("%lld", &n);
        printf("Case #%d: %lld\n", i, max_value(n));

    }

    return 0;
}
