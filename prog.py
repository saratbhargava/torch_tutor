import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    parser.add_argument("--echo", type=str,
                        default="sarat", help='Write something here')
    parser.add_argument("squared", type=int, default=2,
                        help='Square the number')
    group.add_argument("-v", "--verbose", help="Increase the verbosity",
                        action="store_true")
    group.add_argument("-q", "--quiet", help="Silent display", action="store_true")
    args = parser.parse_args()

    print(args.echo)

    print(args.squared**2)

    if args.quiet:
        print("silence mode is on:)")
    
    if args.verbose:
        print("verbose mode is on!")
