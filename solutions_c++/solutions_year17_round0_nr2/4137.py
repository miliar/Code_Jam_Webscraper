#include <bits/stdc++.h>
using namespace std;

#define ARRAY_LEN(array) (sizeof(array) / sizeof(*array))
#define SIZEOF_MEMBER(type, member) (sizeof(((type *) NULL)->member))

template <typename T>
T gcd(T x, T y) {
	return y == 0 ? x : gcd(y, x % y);
}

template <typename T>
T clamp(T input, T min, T max) {
	assert(max >= min);

	if (input < min)
		return min;
	else if (input > max)
		return max;
	else
		return input;
}

template <typename T>
T mod(T num, T modulus) { // "Mathematical" modulo, e.g. -2 mod 5 == 3.
	return (num % modulus + modulus) % modulus;
}

int ffs(long long x) { // Find First Set -- 1 + index of the rightmost 1-bit; 0 if all bits are 0.
	return __builtin_ffsll(x);
}

int popcount(long long x) { // Count the number of 1-bits.
	return __builtin_popcountll(x);
}

// UNTESTED
// When using num_to_str, you probably want to immediately strdup or strdupa the result.
//#define NUM_128
#if defined(NUM_128)
	typedef int64_t Num;

	char num_to_str_buffer[21] = {0};
	char *num_to_str(
		Num num, char *buffer = num_to_str_buffer,
		size_t buffer_len = ARRAY_LEN(num_to_str_buffer)) {

		int n_chars_written = snprintf(buffer, buffer_len, "%" PRId64, num);
		assert(n_chars_written < buffer_len);
		return buffer;
	}

	Num num_from_str(const char *str) {
		Num result;
		int state = sscanf(str, "%" SCNd64, &result);
		assert(state != EOF);
		return result;
	}
#else
	typedef __int128 int128_t;
	typedef unsigned __int128 uint128_t;

	typedef int128_t Num;

	char num_to_str_buffer[41] = {0};
	char *num_to_str(
		Num num, char *buffer = num_to_str_buffer,
		size_t buffer_len = ARRAY_LEN(num_to_str_buffer)) {

		bool negative = num < 0;
		if (negative)
			num = -num;

		// Character to write to next. Initially the one before the null terminator.
		char *next = buffer + buffer_len - 2;

		do {
			*(next--) = '0' + (num % 10);
			num /= 10;
		} while (num != 0);

		if (negative)
			*(next--) = '-';

		assert(next + 1 >= buffer);
		return next + 1;
	}

	Num num_from_str(const char *str) {
		bool negative = str[0] == '-';
		if (negative)
			str++;

		Num result = 0;
		for (int i = 0; str[i] != '\0'; i++)
			result = result * 10 + (str[i] - '0');

		return negative ? -result : result;
	}
#endif

void str_rstrip(char *input) {
	size_t length = strlen(input);
	if (length == 0)
		return;

	char *last = input + length - 1;
	while (last >= input && isspace(*last))
		last--;
	*(last + 1) = '\0';
}

char *str_strip(char *input) {
	while (*input != '\0' && isspace(*input))
		input++;
	str_rstrip(input);
	return input;
}

//#define NDEBUG // Disable assertions.

bool debug = true;
#define DEBUG_WRAP(...) \
	do { if (debug) { \
			fflush(stdout); \
			fprintf(stderr, "[D] %s:%d:%s: ", __FILE__, __LINE__, __func__); \
			__VA_ARGS__; \
			fflush(stderr); \
		} } while(0)
#define DEBUG(fmt, ...) DEBUG_WRAP(fprintf(stderr, fmt "\n", ##__VA_ARGS__))
#define DUMP(expr) DEBUG_WRAP(cerr << #expr << " = " << (expr) << "\n")

/************************************************
 *************** End of template. ***************
 ************************************************/


void handle_case(int case_num) {
	char line[4096];
	fgets(line, sizeof(line), stdin);
	str_rstrip(line);

	char *first = line;
	char *last = line + strlen(line) - 1; // Last digit.
	for (char *curr = last; curr > first; curr--) {
		if (curr[-1] > curr[0]) {
			curr[-1]--; // Assumption: no leading zeroes in input.
			memset(curr, '9', last - curr + 1);
		}
	}

	while (*first == '0')
		first++;

	fputs(first, stdout);
}

int main(void) {
	char n_cases_str[64];
	fgets(n_cases_str, sizeof(n_cases_str), stdin);
	int n_cases;
	sscanf(n_cases_str, " %d ", &n_cases);

	for (int case_num = 1; case_num <= n_cases; case_num++) {
		printf("Case #%d: ", case_num);
		handle_case(case_num);
		printf("\n");
	}

	return 0;
}
